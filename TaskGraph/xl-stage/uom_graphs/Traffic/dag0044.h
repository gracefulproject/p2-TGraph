	//dag0044

	int map[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};

	#define MAX_DEGREE 2

	int t_info[] =
	{

	//Node 0
		//Target Map
		1, -1,
		//Target Count
		2, -1,
		//Source Map
		0, -1,
		//Source Count
		3, -1,
		-1, -1,
	//Node 1
		//Target Map
		2, 3,
		//Target Count
		2, 4,
		//Source Map
		0, -1,
		//Source Count
		1, -1,
		4, -1,
	//Node 2
		//Target Map
		4, 5,
		//Target Count
		3, 3,
		//Source Map
		1, -1,
		//Source Count
		2, -1,
		3, -1,
	//Node 3
		//Target Map
		4, -1,
		//Target Count
		1, -1,
		//Source Map
		1, -1,
		//Source Count
		2, -1,
		-1, -1,
	//Node 4
		//Target Map
		6, 7,
		//Target Count
		3, 4,
		//Source Map
		2, 3,
		//Source Count
		1, 1,
		-1, 2,
	//Node 5
		//Target Map
		6, -1,
		//Target Count
		3, -1,
		//Source Map
		2, -1,
		//Source Count
		6, -1,
		-1, -1,
	//Node 6
		//Target Map
		8, -1,
		//Target Count
		3, -1,
		//Source Map
		4, 5,
		//Source Count
		3, 1,
		-1, -1,
	//Node 7
		//Target Map
		8, -1,
		//Target Count
		2, -1,
		//Source Map
		4, -1,
		//Source Count
		7, -1,
		-1, -1,
	//Node 8
		//Target Map
		8, -1,
		//Target Count
		1, -1,
		//Source Map
		6, 7,
		//Source Count
		5, 1,
		-1, -1,
	-2
	};
