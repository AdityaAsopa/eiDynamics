gridSize = 24
separationStyle = 'hex'
sparsity = 2 # denotes how close together the squares can be, sparsity of 1 means a chessboard pattern
totalCoords = 45

_1sqCoords = [147,243,339,435,101,197,293,389,485,151,247,343,439,105,201,
            297,393,489,155,251,347,443,109,205,301,397,493,159,255,351,
            447,113,209,305,401,497,163,259,355,451,117,213,309,405,501]

'''Check allCells.xslx sheet for details'''
patternID ={1	:[101],														
            2	:[105],														
            3	:[109],														
            4	:[113],														
            5	:[117],														
            6	:[147],														
            7	:[151],														
            8	:[155],														
            9	:[159],														
            10	:[163],														
            11	:[197],														
            12	:[201],														
            13	:[205],														
            14	:[209],														
            15	:[213],														
            16	:[243],														
            17	:[247],														
            18	:[251],														
            19	:[255],														
            20	:[259],														
            21	:[293],														
            22	:[297],														
            23	:[301],														
            24	:[305],														
            25	:[309],														
            26	:[339],														
            27	:[343],														
            28	:[347],														
            29	:[351],													
            30	:[355],														
            31	:[389],														
            32	:[393],														
            33	:[397],														
            34	:[401],														
            35	:[405],														
            36	:[435],														
            37	:[439],														
            38	:[443],														
            39	:[447],														
            40	:[451],														
            41	:[485],														
            42	:[489],														
            43	:[493],														
            44	:[497],														
            45	:[501],														
            46	:[209,247,259,301,393],										
            47	:[205,251,297,389,447],										
            48	:[197,255,347,401,439],										
            49	:[201,293,351,355,443],										
            50	:[251,305,343,397,451],										
            51	:[105,109,113,117,155,159,243,309,343,351,355,405,443,451,485],
            52	:[101,109,117,147,155,197,305,309,339,343,351,401,451,485,497],
            53	:[151,163,197,201,209,213,259,301,339,347,393,401,435,439,489],
            54	:[113,159,205,209,243,251,255,301,347,355,393,405,439,443,447],
            55	:[105,151,163,201,213,247,259,293,297,389,397,435,489,493,501],
            56	:[101,113,147,159,209,243,485],								
            57	:[101,113,159,205,209,213,497],								
            58	:[147,163,209,243,255,443,485],								
            59	:[109,201,247,301,309,355,501],								
            60	:[117,151,259,347,351,389,439],								
            61	:[163,197,201,247,301,447,501],								
            62	:[117,151,259,355,393,405,439],								
            63	:[105,117,339,347,351,389,493],								
            64	:[147,163,197,255,443,447,501],								
            65	:[109,201,309,355,393,405,439],								
            66	:[101,205,213,397,401,451,497],								
            67	:[155,251,293,297,305,489,493],								
            68	:[105,293,297,339,389,489,493],								
            69	:[155,251,305,343,435,451,489],								
            70	:[305,343,397,401,435,451,497],								
            71	:[101,113,147,159,163,197,205,209,213,243,255,443,447,485,501],
            72	:[101,113,147,159,205,209,213,243,255,343,397,401,451,485,497],
            73	:[109,147,163,197,201,209,243,247,255,301,309,443,447,485,501],
            74	:[109,117,151,201,247,259,301,309,347,351,355,389,393,405,439],
            75	:[101,113,155,159,205,213,251,305,343,397,401,435,451,489,497],
            76	:[105,117,155,251,259,293,297,305,339,347,351,389,435,489,493],
            77	:[109,151,163,197,201,247,301,309,355,393,405,439,443,447,501],
            78	:[105,117,151,259,293,297,339,347,351,355,389,393,405,439,493],
            79	:[105,155,251,293,297,305,339,343,397,401,435,451,489,493,497],
            80	:[101,147,197,243,293,339,435],							
            81	:[105,151,201,247,297,343,439],							
            82	:[109,155,205,251,301,347,443],							
            83	:[113,159,209,255,305,351,447],							
            84	:[117,163,213,259,309,355,451],							
            85	:[101,151,197,293,389,435,485],							
            86	:[105,155,201,297,393,439,489],							
            87	:[109,159,205,301,397,443,493],							
            88	:[113,163,209,305,401,447,497],							
            89	:[117,147,213,309,405,451,501],							
            90	:[151,247,293,343,389,439,485],							
            91	:[155,251,297,347,393,443,489],							
            92	:[147,243,309,339,405,435,501],							
            93	:[159,255,301,351,397,447,493],							
            94	:[163,259,305,355,401,451,497],							
            95	:[101,105,147,151,197,201,243,247,293,339,343,389,435,439,485],
            96	:[105,109,155,201,205,247,251,297,301,343,347,393,439,443,489],
            97	:[101,117,147,151,197,213,243,293,309,339,389,405,435,485,501],
            98	:[105,151,155,197,201,247,251,293,297,343,389,393,439,485,489],
            99	:[109,113,159,205,209,255,301,305,347,351,397,401,443,447,493],
            100	:[101,117,147,163,213,243,259,309,339,355,405,435,451,497,501],
            101	:[109,155,159,205,251,255,297,301,347,351,393,397,443,489,493],
            102	:[113,117,163,209,213,259,305,309,355,401,405,447,451,497,501],
            103	:[113,159,163,209,255,259,305,351,355,397,401,447,451,493,497]}

def givePatternID(sqSet):
    for k,v in patternID.items():
        if v==sqSet:
            return int(k)