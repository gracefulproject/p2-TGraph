	//dag0015

	int map[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};

	#define MAX_DEGREE 3

	int t_info[] =
	{

	//Node 0
		//Target Map
		1, 2, 3,
		//Target Count
		5, 5, 3,
		//Source Map
		0, -1, -1,
		//Source Count
		2, -1, -1,
		2, -1, -1,
		4, -1, -1,
	//Node 1
		//Target Map
		4, 5, -1,
		//Target Count
		1, 5, -1,
		//Source Map
		0, -1, -1,
		//Source Count
		3, -1, -1,
		2, -1, -1,
		-1, -1, -1,
	//Node 2
		//Target Map
		4, -1, -1,
		//Target Count
		2, -1, -1,
		//Source Map
		0, -1, -1,
		//Source Count
		2, -1, -1,
		-1, -1, -1,
		-1, -1, -1,
	//Node 3
		//Target Map
		4, -1, -1,
		//Target Count
		3, -1, -1,
		//Source Map
		0, -1, -1,
		//Source Count
		1, -1, -1,
		-1, -1, -1,
		-1, -1, -1,
	//Node 4
		//Target Map
		6, -1, -1,
		//Target Count
		5, -1, -1,
		//Source Map
		1, 2, 3,
		//Source Count
		1, 4, 3,
		-1, -1, -1,
		-1, -1, -1,
	//Node 5
		//Target Map
		6, -1, -1,
		//Target Count
		1, -1, -1,
		//Source Map
		1, -1, -1,
		//Source Count
		2, -1, -1,
		-1, -1, -1,
		-1, -1, -1,
	//Node 6
		//Target Map
		7, -1, -1,
		//Target Count
		1, -1, -1,
		//Source Map
		4, 5, -1,
		//Source Count
		2, 4, -1,
		-1, -1, -1,
		-1, -1, -1,
	//Node 7
		//Target Map
		8, -1, -1,
		//Target Count
		1, -1, -1,
		//Source Map
		6, -1, -1,
		//Source Count
		1, -1, -1,
		-1, -1, -1,
		-1, -1, -1,
	//Node 8
		//Target Map
		8, -1, -1,
		//Target Count
		3, -1, -1,
		//Source Map
		7, -1, -1,
		//Source Count
		2, -1, -1,
		-1, -1, -1,
		-1, -1, -1,
	-2
	};
