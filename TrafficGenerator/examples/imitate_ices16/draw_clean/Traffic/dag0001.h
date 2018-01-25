	//dag0001

	int map[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};

	#define MAX_DEGREE 5

	int t_info[] =
	{

	//Node 0
		//Target Map
		1, 2, 6, 4, -1,
		//Target Count
		8, 3, 1, 3, -1,
		//Source Map
		0, -1, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		2, -1, -1, -1, -1,
		1, -1, -1, -1, -1,
		2, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 1
		//Target Map
		9, -1, -1, -1, -1,
		//Target Count
		1, -1, -1, -1, -1,
		//Source Map
		0, -1, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 2
		//Target Map
		3, 6, -1, -1, -1,
		//Target Count
		7, 2, -1, -1, -1,
		//Source Map
		0, -1, -1, -1, -1,
		//Source Count
		3, -1, -1, -1, -1,
		3, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 3
		//Target Map
		9, 5, 6, 4, -1,
		//Target Count
		1, 2, 2, 2, -1,
		//Source Map
		2, -1, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		4, -1, -1, -1, -1,
		5, -1, -1, -1, -1,
		1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 4
		//Target Map
		8, -1, -1, -1, -1,
		//Target Count
		4, -1, -1, -1, -1,
		//Source Map
		0, 3, -1, -1, -1,
		//Source Count
		3, 5, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 5
		//Target Map
		11, 7, 6, 10, -1,
		//Target Count
		3, 10, 2, 4, -1,
		//Source Map
		3, -1, -1, -1, -1,
		//Source Count
		4, -1, -1, -1, -1,
		1, -1, -1, -1, -1,
		1, -1, -1, -1, -1,
		2, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 6
		//Target Map
		8, 13, -1, -1, -1,
		//Target Count
		3, 4, -1, -1, -1,
		//Source Map
		0, 2, 3, 5, -1,
		//Source Count
		2, 4, -1, 4, -1,
		-1, -1, 4, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 7
		//Target Map
		9, 15, -1, -1, -1,
		//Target Count
		5, 3, -1, -1, -1,
		//Source Map
		5, -1, -1, -1, -1,
		//Source Count
		4, -1, -1, -1, -1,
		4, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 8
		//Target Map
		11, 12, 10, -1, -1,
		//Target Count
		1, 6, 3, -1, -1,
		//Source Map
		4, 6, -1, -1, -1,
		//Source Count
		1, -1, -1, -1, -1,
		-1, 4, -1, -1, -1,
		-1, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 9
		//Target Map
		12, 14, -1, -1, -1,
		//Target Count
		5, 3, -1, -1, -1,
		//Source Map
		1, 3, 7, -1, -1,
		//Source Count
		3, -1, 2, -1, -1,
		-1, 3, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 10
		//Target Map
		15, 16, -1, -1, -1,
		//Target Count
		1, 5, -1, -1, -1,
		//Source Map
		5, 8, -1, -1, -1,
		//Source Count
		-1, 1, -1, -1, -1,
		2, 4, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 11
		//Target Map
		19, -1, -1, -1, -1,
		//Target Count
		4, -1, -1, -1, -1,
		//Source Map
		5, 8, -1, -1, -1,
		//Source Count
		2, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 12
		//Target Map
		17, 14, 13, -1, -1,
		//Target Count
		3, 1, 3, -1, -1,
		//Source Map
		8, 9, -1, -1, -1,
		//Source Count
		1, -1, -1, -1, -1,
		-1, 1, -1, -1, -1,
		-1, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 13
		//Target Map
		22, 21, 16, -1, -1,
		//Target Count
		2, 1, 3, -1, -1,
		//Source Map
		12, 6, -1, -1, -1,
		//Source Count
		-1, 1, -1, -1, -1,
		2, 4, -1, -1, -1,
		-1, 3, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 14
		//Target Map
		17, 22, 21, -1, -1,
		//Target Count
		4, 3, 2, -1, -1,
		//Source Map
		12, 9, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		1, 4, -1, -1, -1,
		-1, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 15
		//Target Map
		23, -1, -1, -1, -1,
		//Target Count
		3, -1, -1, -1, -1,
		//Source Map
		10, 7, -1, -1, -1,
		//Source Count
		1, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 16
		//Target Map
		21, 18, 20, 23, -1,
		//Target Count
		4, 2, 1, 4, -1,
		//Source Map
		10, 13, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		5, -1, -1, -1, -1,
		-1, 6, -1, -1, -1,
		-1, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 17
		//Target Map
		19, 23, -1, -1, -1,
		//Target Count
		4, 2, -1, -1, -1,
		//Source Map
		12, 14, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		-1, 1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 18
		//Target Map
		23, -1, -1, -1, -1,
		//Target Count
		2, -1, -1, -1, -1,
		//Source Map
		16, -1, -1, -1, -1,
		//Source Count
		2, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 19
		//Target Map
		22, -1, -1, -1, -1,
		//Target Count
		2, -1, -1, -1, -1,
		//Source Map
		11, 17, -1, -1, -1,
		//Source Count
		2, 3, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 20
		//Target Map
		21, 24, -1, -1, -1,
		//Target Count
		1, 1, -1, -1, -1,
		//Source Map
		16, -1, -1, -1, -1,
		//Source Count
		3, -1, -1, -1, -1,
		3, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 21
		//Target Map
		22, 24, 23, -1, -1,
		//Target Count
		2, 4, 2, -1, -1,
		//Source Map
		13, 14, 16, 20, -1,
		//Source Count
		4, -1, -1, -1, -1,
		-1, 2, 2, -1, -1,
		-1, -1, -1, 3, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 22
		//Target Map
		24, -1, -1, -1, -1,
		//Target Count
		4, -1, -1, -1, -1,
		//Source Map
		13, 14, 19, 21, -1,
		//Source Count
		1, 4, 3, 5, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 23
		//Target Map
		24, -1, -1, -1, -1,
		//Target Count
		6, -1, -1, -1, -1,
		//Source Map
		15, 16, 17, 18, 21,
		//Source Count
		5, 3, 1, 6, 1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	//Node 24
		//Target Map
		24, -1, -1, -1, -1,
		//Target Count
		1, -1, -1, -1, -1,
		//Source Map
		20, 21, 22, 23, -1,
		//Source Count
		3, 3, 2, 1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1,
	-2
	};
