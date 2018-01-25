#ifndef DEFTGSDP_H
#define DEFTGSDP_H

/* deftgsdp.h
 * Contains basic macro and type definitions.
 * */

/*-------------------------------------------------------------------*/
/*--------------------- basic information ---------------------------*/
#define MAJOR_VERSION			1
#define MINOR_VERSION			0
#define BOARD_SYSTEM			103		// corresponds to machine 102, 103, 104 etc

/*-------------------------------------------------------------------*/
/*------------------ additional configuration------------------------*/
#if(BOARD_SYSTEM==102)
#define MAX_NUM_NODES			3		// SpiN3
#elif(BOARD_SYSTEM==103)
#define MAX_NUM_NODES			47		// Spin4 or Spin5 board
#elif(BOARD_SYSTEM==1033)
#define MAX_NUM_NODES			143		// special case with 3 Spin5 boards
/*
 * Big Question: how to handle bigger machine?
 * It won't be feasible to be handled by a single chip as a root-monitor
#elif(BOARD_SYSTEM==104)
#define MAX_NUM_NODES			1151	// 24 Spin5 boards in a frame
#elif(BOARD_SYSTEM==105)
#define MAX_NUM_NODES			5759	// 1 cabinet (5 frames)
#elif(BOARD_SYSTEM==106)
#define MAX_NUM_NODES			57599	// the 10 cabinet
*/
#else
#define MAX_NUM_NODES			0		// invalid configuration
#endif

/*-------------------------------------------------------------------*/
/*------------- priority assignment for API callback ----------------*/
#define PRIORITY_SDP			0
#define PRIORITY_REPORTING		3						// whoaaa, spin1_schedule_callback() DOESN'T work with priority 5????
#define PRIORITY_TIMER			-1
#define PRIORITY_PROCESSING		2

/*-------------------------------------------------------------------*/
/*----------------- for sdp commucation mechanism -------------------*/
#define TGPKT_PING					0x7179					// for debugging, why some chips produce WDOG???
#define DEF_TIMEOUT					10
#define TGPKT_NORMAL_ID				1
#define TGPKT_HOST_ASK_REPORT		0x2ead
#define TGPKT_CHIP_NODE_MAP			0xc01e
#define TGPKT_DEPENDENCY			0xdec1
#define TGPKT_SOURCE_TARGET			0x52ce
#define TGPKT_START_SIMULATION		0x6060
#define TGPKT_STOP_SIMULATION		0x7070
#define TGPKT_HOST_SEND_TICK		0x71c4
#define TGPKT_NODE_SEND_HIST_RPT	0x4127
#define TGPKT_NODE_SEND_HIST_IPTAG	1
#define DEF_CORE					1
#define DEF_SEND_PORT				1						// a node will send the packet out through this port
#define DEF_RECV_PORT				2						// a node will receive packet from others via this port
#define DEF_SENDACK_PORT			3						// a node will send an acknowledge to the sender via this port
#define DEF_RECVACK_PORT			4
#define DEF_CONF_PORT				7						// default configuration port used by the host to configure aplx
#define SOURCE_SINK_NODE_ID			0xFFFF
// regarding mapping/monitoring
#define TGPKT_HOST_REQ_RESOURCE		0x50ce					// host-PC send request for resources to root-monitor
#define DEF_MONITOR_CORE			1


typedef struct {
	uchar x;
	uchar y;
} chip_coord_t;

#endif // DEFTGSDP_H
