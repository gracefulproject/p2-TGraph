/* SYNOPSIS: Try to modify p2p table so that it only use 4 direction (not 6)
*/
#include <sark.h>

#define EAST 		0
#define NORTHEAST 	1
#define NORTH		2
#define WEST		3
#define SOUTHWEST	4
#define SOUTH		5
#define NONE		6
#define LOCAL		7

ushort myX, myY;

int abs(int val)
{
	int _abs_ = val;
	if(val < 0) _abs_ = 0 - val;
	return _abs_;
}

void read_table()
{
	ushort i;
	uint entry;
	for(i=0; i<0xFFFF; i++) {
		entry = rtr_p2p_get(i);
		if(entry != NONE) {
			io_printf(IO_BUF, "Direction to chip-%d at <%d,%d>: %d\n",
					i, CHIP_X(i), CHIP_Y(i), entry);
		}
	}
}

uint isLinkOK(uint DIR)
{
	uint found = 0;
	uint entry;
	for(ushort i=0; i<0xFFFF; i++) {
		entry = rtr_p2p_get(i);
		if(entry==DIR) {
			found = 1; 
			break;
		}
	}
	return found;
}

void set_to_quad_grid()
{
	ushort i, x, y;
	uint entry;
	int dx, dy;
	uint dir;
	// scan for all entry in the p2p table
	for(i=0; i<0xFFFF; i++){
		entry = rtr_p2p_get(i);
		x = CHIP_X(i);
		y = CHIP_Y(i);
		dx = (int)x - (int)myX;
		dy = (int)y - (int)myY;
		// ignore entry 6 (drop) and 7 (itself)
		
		if(entry==NORTHEAST || entry==SOUTHWEST) {

			// NOTE: the followind disabled lines don't work, since they
			//		 don't check dead links
			/*
			if(dx==0) {
				// up or down
				dir = (y > myY) ? NORTH : SOUTH;
			} 
			else if(dy==0) {
				dir = (x > myX) ? EAST : WEST;
			}
			else {
				// prefer horizontal direction
				if(abs(dx) <= abs(dy)) {
					dir = (x > myX) ? EAST : WEST;
				}
				else {
					dir = (y > myY) ? NORTH : SOUTH;
				}
			}
			*/
			/*
			if(dx==0 || (abs(dx) <= abs(dy))) {
				dir = (y > myY) ? NORTH : SOUTH;
			}
			else {
				dir = (x > myX) ? EAST : WEST;
			}*/
			/*
			io_printf(IO_BUF, "entry=%d,myX=%d,myY=%d\tx=%d,y=%d\t,dx=%d,dy=%d,\tdir=%d\n",
						entry,myX,myY,x,y,dx,dy,dir);
			*/

			if(entry==NORTHEAST) {
				if(isLinkOK(EAST))
					dir = EAST;
				else
					dir = NORTH;
			}
			if(entry==SOUTHWEST) {
				if(isLinkOK(WEST))
					dir = WEST;
				else
					dir = SOUTH;
			}
			rtr_p2p_set(i, dir);
		}
	}
}

void c_main()
{
	myX = CHIP_X(sv->p2p_addr);
	myY = CHIP_Y(sv->p2p_addr);
	io_printf(IO_BUF, "Original table:\n----------------\n");
	read_table();
	set_to_quad_grid();
	io_printf(IO_BUF, "Modified table:\n----------------\n");
	read_table();
}

