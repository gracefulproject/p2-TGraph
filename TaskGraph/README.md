# Graceful_SpinTG
Task Graph implementation on SpiNNaker

## Directory structure:
- aplx: source codes for SpiNNaker program
- host: source codes for python program
- xl-stage: program that generates task graph (from York)

## General scenario:
1. Chip <0,0> will be considered as the the "Regional" supervisor program (REGSVP). It has:
  - core-1: root-profiler (from other project)
  - core-2: root-monitor
  - core-3..12: source/sink of up to 10 networks
  - core-13..17: optimizer: dynamic mapper, etc
  REGSVP is supposed to run constantly at 200MHz in order to have a "fix" clock for synchronization (by the profiler)
2. Other chips are for TG processing. Each chip has:
  - core-1: sub-profiler (from other project)
  - core-2: sub-monitor
  - core-3..17: tgsdp, a.k.a processing elements (PE)
3. Host-PC will interact with the REGSVP:
  - Host-PC sends network topology to REGSVP (Monitor-node) along with the dependency list (as a data structure)
  - REGSVP confirms if it has enough resources (#Nodes). If it has, then start mapping according to the mapping algorithm: GA, etc. Then report back to host-PC:
    - the resulting map
    - graph ID
    - the SOURCE/SINK core number
  - Host-PC sends data to SOURCE-core (depends on the allocated one by the root-monitor). SOURCE-node delivers data to corresponding nodes.
  - REGSVP propagates certain final output from one or more SINK-core(s) (from one or more TG node(s)) to the host-PC.

## Possible scenario:
1. Multiple TG running on the same machine (only if resource, a.k.a #Nodes, is available). Max. graphs: 10

## REGSVP components:
1. Root-Monitor:
   - receives network structure from host-PC and do initial mapping
   - invokes optimizer to do dynamic mapping later on, do process migration, etc.
2. Root-Profiler (from other project, such as t6-readSpin4Power):
   - generates global clock syncronizer
   - Measure temperature, frequency
   - receives info from node's profiler, combine all information, and send to host-PC
3. Source/Sink:
   - receives/sends packet from/to host-PC

## Each node components:
1. Sub-Monitor:
   - count the P2P traffic and, if possible in the future, do the traffic management:
     it will consider the load of other node before modifying the P2P routing table
   - report to REGSVP about the number of available PE, so that the REGSVP can decide
     which task node will be assigned to this chip.
     A task may have n-output link; hence, it requires n-cores in that chip.
2. Sub-Profiler:
   - Measure temperature
   - Measure and alter chip's frequency
   - Synchronize clock (from Master Profiler in chip REGSVP)
   - Measure CPU load
   - Send all information to Master Profiler
3. Tgsdp, a.k.a PE (processing elements):
   - each core corresponds to one task output; hence, a task node has a max 15 output
