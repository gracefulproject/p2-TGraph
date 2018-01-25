#ifndef MONITOR_H
#define MONITOR_H

/* Provides basic macro, variables and function declaration ONLY for monitoring node.
 * */

#include "deftgsdp.h"



/*--------------------- Related with currently running task graph on machine -----------------------*/

#define MAX_RUNNING_TG	10	// maximum number of application TG running simultaneously in a machine
// running_graph_t keeps track of currently running task graph on a machine
typedef struct {
	uchar idTG;		// assigned task graph ID
	uchar numNodes;	// number of nodes in this task graph
	uchar SScore;	// assigned sink/source core
	chip_coord_t pos[MAX_NODES_NUM];
} running_graph_t;
running_graph_t running_TG[MAX_RUNNING_TG];

uchar numRunningTG;
uchar numFreeNodes;

void hTimer_monitor(uint tick, uint Null);
void hSDP_monitor(uint mBox, uint port);

#endif // MONITOR_H
