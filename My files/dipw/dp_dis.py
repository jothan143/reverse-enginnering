# Disassemble At : Fri Aug 14 18:35:35 2020
# Method Name : <module> 
# File Name : dp.pyc

  1           0 LOAD_CONST               1 (<code object main at 0xaed4be78, file "<string>", line 1>)
              3 MAKE_FUNCTION            0
              6 STORE_NAME               0 (main)

  4           9 LOAD_NAME                1 (__name__)
             12 LOAD_CONST               2 ('__main__')
             15 COMPARE_OP               2 (==)
             18 POP_JUMP_IF_FALSE       31

  5          21 LOAD_NAME                0 (main)
             24 CALL_FUNCTION            0
             27 POP_TOP             
             28 JUMP_FORWARD             0 (to 31)
        >>   31 LOAD_CONST               0 (None)
             34 RETURN_VALUE        

# source code ++
#
# def main():
#	password = 'Call me a Python virtual machine! I can interpret Python bytecodes!!!'
#	if raw_input("password: ") == password:
# 		print 'hitcon{Now you can compile and run Python bytecode in your brain!}'
#	else:
#		print 'Wrong password... Please try again. Do not brute force. =)'
#
# if __name__=="__main__":
# 	main()

# Disassemble At : Fri Aug 14 18:35:35 2020
# Method Name : main 
# File Name : dp.pyc

  1           0 LOAD_GLOBAL              0 (chr)
              3 LOAD_CONST               1 (108)
              6 CALL_FUNCTION            1
              9 LOAD_GLOBAL              0 (chr)
             12 LOAD_CONST               1 (108)
             15 CALL_FUNCTION            1
             18 LOAD_GLOBAL              0 (chr)
             21 LOAD_CONST               2 (97)
             24 CALL_FUNCTION            1
             27 LOAD_GLOBAL              0 (chr)
             30 LOAD_CONST               3 (67)
             33 CALL_FUNCTION            1
             36 ROT_TWO             
             37 BINARY_ADD          
             38 ROT_TWO             
             39 BINARY_ADD          
             40 ROT_TWO             
             41 BINARY_ADD          
             42 LOAD_GLOBAL              0 (chr)
             45 LOAD_CONST               4 (32)
             48 CALL_FUNCTION            1
             51 LOAD_GLOBAL              0 (chr)
             54 LOAD_CONST               5 (101)
             57 CALL_FUNCTION            1
             60 LOAD_GLOBAL              0 (chr)
             63 LOAD_CONST               6 (109)
             66 CALL_FUNCTION            1
             69 LOAD_GLOBAL              0 (chr)
             72 LOAD_CONST               4 (32)
             75 CALL_FUNCTION            1
             78 ROT_TWO             
             79 BINARY_ADD          
             80 ROT_TWO             
             81 BINARY_ADD          
             82 ROT_TWO             
             83 BINARY_ADD          
             84 BINARY_ADD          
             85 LOAD_GLOBAL              0 (chr)
             88 LOAD_CONST               7 (121)
             91 CALL_FUNCTION            1
             94 LOAD_GLOBAL              0 (chr)
             97 LOAD_CONST               8 (80)
            100 CALL_FUNCTION            1
            103 LOAD_GLOBAL              0 (chr)
            106 LOAD_CONST               4 (32)
            109 CALL_FUNCTION            1
            112 LOAD_GLOBAL              0 (chr)
            115 LOAD_CONST               2 (97)
            118 CALL_FUNCTION            1
            121 ROT_TWO             
            122 BINARY_ADD          
            123 ROT_TWO             
            124 BINARY_ADD          
            125 ROT_TWO             
            126 BINARY_ADD          
            127 LOAD_GLOBAL              0 (chr)
            130 LOAD_CONST               9 (104)
            133 CALL_FUNCTION            1
            136 LOAD_GLOBAL              0 (chr)
            139 LOAD_CONST              10 (116)
            142 CALL_FUNCTION            1
            145 ROT_TWO             
            146 BINARY_ADD          
            147 LOAD_GLOBAL              0 (chr)
            150 LOAD_CONST               4 (32)
            153 CALL_FUNCTION            1
            156 LOAD_GLOBAL              0 (chr)
            159 LOAD_CONST              11 (110)
            162 CALL_FUNCTION            1
            165 LOAD_GLOBAL              0 (chr)
            168 LOAD_CONST              12 (111)
            171 CALL_FUNCTION            1
            174 ROT_TWO             
            175 BINARY_ADD          
            176 ROT_TWO             
            177 BINARY_ADD          
            178 BINARY_ADD          
            179 BINARY_ADD          
            180 BINARY_ADD          
            181 LOAD_GLOBAL              0 (chr)
            184 LOAD_CONST              10 (116)
            187 CALL_FUNCTION            1
            190 LOAD_GLOBAL              0 (chr)
            193 LOAD_CONST              13 (114)
            196 CALL_FUNCTION            1
            199 LOAD_GLOBAL              0 (chr)
            202 LOAD_CONST              14 (105)
            205 CALL_FUNCTION            1
            208 LOAD_GLOBAL              0 (chr)
            211 LOAD_CONST              15 (118)
            214 CALL_FUNCTION            1
            217 ROT_TWO             
            218 BINARY_ADD          
            219 ROT_TWO             
            220 BINARY_ADD          
            221 ROT_TWO             
            222 BINARY_ADD          
            223 LOAD_GLOBAL              0 (chr)
            226 LOAD_CONST               4 (32)
            229 CALL_FUNCTION            1
            232 LOAD_GLOBAL              0 (chr)
            235 LOAD_CONST               1 (108)
            238 CALL_FUNCTION            1
            241 LOAD_GLOBAL              0 (chr)
            244 LOAD_CONST               2 (97)
            247 CALL_FUNCTION            1
            250 LOAD_GLOBAL              0 (chr)
            253 LOAD_CONST              16 (117)
            256 CALL_FUNCTION            1
            259 ROT_TWO             
            260 BINARY_ADD          
            261 ROT_TWO             
            262 BINARY_ADD          
            263 ROT_TWO             
            264 BINARY_ADD          
            265 BINARY_ADD          
            266 LOAD_GLOBAL              0 (chr)
            269 LOAD_CONST               9 (104)
            272 CALL_FUNCTION            1
            275 LOAD_GLOBAL              0 (chr)
            278 LOAD_CONST              17 (99)
            281 CALL_FUNCTION            1
            284 LOAD_GLOBAL              0 (chr)
            287 LOAD_CONST               2 (97)
            290 CALL_FUNCTION            1
            293 LOAD_GLOBAL              0 (chr)
            296 LOAD_CONST               6 (109)
            299 CALL_FUNCTION            1
            302 ROT_TWO             
            303 BINARY_ADD          
            304 ROT_TWO             
            305 BINARY_ADD          
            306 ROT_TWO             
            307 BINARY_ADD          
            308 LOAD_GLOBAL              0 (chr)
            311 LOAD_CONST              11 (110)
            314 CALL_FUNCTION            1
            317 LOAD_GLOBAL              0 (chr)
            320 LOAD_CONST              14 (105)
            323 CALL_FUNCTION            1
            326 ROT_TWO             
            327 BINARY_ADD          
            328 LOAD_GLOBAL              0 (chr)
            331 LOAD_CONST               4 (32)
            334 CALL_FUNCTION            1
            337 LOAD_GLOBAL              0 (chr)
            340 LOAD_CONST              18 (33)
            343 CALL_FUNCTION            1
            346 LOAD_GLOBAL              0 (chr)
            349 LOAD_CONST               5 (101)
            352 CALL_FUNCTION            1
            355 ROT_TWO             
            356 BINARY_ADD          
            357 ROT_TWO             
            358 BINARY_ADD          
            359 BINARY_ADD          
            360 BINARY_ADD          
            361 BINARY_ADD          
            362 BINARY_ADD          
            363 LOAD_GLOBAL              0 (chr)
            366 LOAD_CONST               2 (97)
            369 CALL_FUNCTION            1
            372 LOAD_GLOBAL              0 (chr)
            375 LOAD_CONST              17 (99)
            378 CALL_FUNCTION            1
            381 LOAD_GLOBAL              0 (chr)
            384 LOAD_CONST               4 (32)
            387 CALL_FUNCTION            1
            390 LOAD_GLOBAL              0 (chr)
            393 LOAD_CONST              19 (73)
            396 CALL_FUNCTION            1
            399 ROT_TWO             
            400 BINARY_ADD          
            401 ROT_TWO             
            402 BINARY_ADD          
            403 ROT_TWO             
            404 BINARY_ADD          
            405 LOAD_GLOBAL              0 (chr)
            408 LOAD_CONST              11 (110)
            411 CALL_FUNCTION            1
            414 LOAD_GLOBAL              0 (chr)
            417 LOAD_CONST              14 (105)
            420 CALL_FUNCTION            1
            423 LOAD_GLOBAL              0 (chr)
            426 LOAD_CONST               4 (32)
            429 CALL_FUNCTION            1
            432 LOAD_GLOBAL              0 (chr)
            435 LOAD_CONST              11 (110)
            438 CALL_FUNCTION            1
            441 ROT_TWO             
            442 BINARY_ADD          
            443 ROT_TWO             
            444 BINARY_ADD          
            445 ROT_TWO             
            446 BINARY_ADD          
            447 BINARY_ADD          
            448 LOAD_GLOBAL              0 (chr)
            451 LOAD_CONST              20 (112)
            454 CALL_FUNCTION            1
            457 LOAD_GLOBAL              0 (chr)
            460 LOAD_CONST              13 (114)
            463 CALL_FUNCTION            1
            466 LOAD_GLOBAL              0 (chr)
            469 LOAD_CONST               5 (101)
            472 CALL_FUNCTION            1
            475 LOAD_GLOBAL              0 (chr)
            478 LOAD_CONST              10 (116)
            481 CALL_FUNCTION            1
            484 ROT_TWO             
            485 BINARY_ADD          
            486 ROT_TWO             
            487 BINARY_ADD          
            488 ROT_TWO             
            489 BINARY_ADD          
            490 LOAD_GLOBAL              0 (chr)
            493 LOAD_CONST               5 (101)
            496 CALL_FUNCTION            1
            499 LOAD_GLOBAL              0 (chr)
            502 LOAD_CONST              13 (114)
            505 CALL_FUNCTION            1
            508 ROT_TWO             
            509 BINARY_ADD          
            510 LOAD_GLOBAL              0 (chr)
            513 LOAD_CONST               8 (80)
            516 CALL_FUNCTION            1
            519 LOAD_GLOBAL              0 (chr)
            522 LOAD_CONST               4 (32)
            525 CALL_FUNCTION            1
            528 LOAD_GLOBAL              0 (chr)
            531 LOAD_CONST              10 (116)
            534 CALL_FUNCTION            1
            537 ROT_TWO             
            538 BINARY_ADD          
            539 ROT_TWO             
            540 BINARY_ADD          
            541 BINARY_ADD          
            542 BINARY_ADD          
            543 BINARY_ADD          
            544 LOAD_GLOBAL              0 (chr)
            547 LOAD_CONST              12 (111)
            550 CALL_FUNCTION            1
            553 LOAD_GLOBAL              0 (chr)
            556 LOAD_CONST               9 (104)
            559 CALL_FUNCTION            1
            562 LOAD_GLOBAL              0 (chr)
            565 LOAD_CONST              10 (116)
            568 CALL_FUNCTION            1
            571 LOAD_GLOBAL              0 (chr)
            574 LOAD_CONST               7 (121)
            577 CALL_FUNCTION            1
            580 ROT_TWO             
            581 BINARY_ADD          
            582 ROT_TWO             
            583 BINARY_ADD          
            584 ROT_TWO             
            585 BINARY_ADD          
            586 LOAD_GLOBAL              0 (chr)
            589 LOAD_CONST               4 (32)
            592 CALL_FUNCTION            1
            595 LOAD_GLOBAL              0 (chr)
            598 LOAD_CONST              11 (110)
            601 CALL_FUNCTION            1
            604 ROT_TWO             
            605 BINARY_ADD          
            606 LOAD_GLOBAL              0 (chr)
            609 LOAD_CONST              10 (116)
            612 CALL_FUNCTION            1
            615 LOAD_GLOBAL              0 (chr)
            618 LOAD_CONST               7 (121)
            621 CALL_FUNCTION            1
            624 LOAD_GLOBAL              0 (chr)
            627 LOAD_CONST              21 (98)
            630 CALL_FUNCTION            1
            633 ROT_TWO             
            634 BINARY_ADD          
            635 ROT_TWO             
            636 BINARY_ADD          
            637 BINARY_ADD          
            638 BINARY_ADD          
            639 LOAD_GLOBAL              0 (chr)
            642 LOAD_CONST              22 (100)
            645 CALL_FUNCTION            1
            648 LOAD_GLOBAL              0 (chr)
            651 LOAD_CONST              12 (111)
            654 CALL_FUNCTION            1
            657 LOAD_GLOBAL              0 (chr)
            660 LOAD_CONST              17 (99)
            663 CALL_FUNCTION            1
            666 LOAD_GLOBAL              0 (chr)
            669 LOAD_CONST               5 (101)
            672 CALL_FUNCTION            1
            675 ROT_TWO             
            676 BINARY_ADD          
            677 ROT_TWO             
            678 BINARY_ADD          
            679 ROT_TWO             
            680 BINARY_ADD          
            681 LOAD_GLOBAL              0 (chr)
            684 LOAD_CONST              23 (115)
            687 CALL_FUNCTION            1
            690 LOAD_GLOBAL              0 (chr)
            693 LOAD_CONST               5 (101)
            696 CALL_FUNCTION            1
            699 ROT_TWO             
            700 BINARY_ADD          
            701 LOAD_GLOBAL              0 (chr)
            704 LOAD_CONST              18 (33)
            707 CALL_FUNCTION            1
            710 LOAD_GLOBAL              0 (chr)
            713 LOAD_CONST              18 (33)
            716 CALL_FUNCTION            1
            719 LOAD_GLOBAL              0 (chr)
            722 LOAD_CONST              18 (33)
            725 CALL_FUNCTION            1
            728 ROT_TWO             
            729 BINARY_ADD          
            730 ROT_TWO             
            731 BINARY_ADD          
            732 BINARY_ADD          
            733 BINARY_ADD          
            734 BINARY_ADD          
            735 BINARY_ADD          
            736 BINARY_ADD          
            737 LOAD_CONST               0 (None)
            740 NOP                 
            741 JUMP_ABSOLUTE          759
        >>  744 LOAD_GLOBAL              1 (raw_input)
            747 JUMP_ABSOLUTE         1480
        >>  750 LOAD_FAST                0 (password)
            753 COMPARE_OP               2 (==)
# if raw_input("password: ") == password
            756 JUMP_ABSOLUTE          767
        >>  759 ROT_TWO             
            760 STORE_FAST               0 (password)
# password = ...
            763 POP_TOP             
            764 JUMP_ABSOLUTE          744
        >>  767 POP_JUMP_IF_FALSE     1591
            770 LOAD_GLOBAL              0 (chr)
            773 LOAD_CONST              17 (99)
            776 CALL_FUNCTION            1
            779 LOAD_GLOBAL              0 (chr)
            782 LOAD_CONST              10 (116)
            785 CALL_FUNCTION            1
            788 LOAD_GLOBAL              0 (chr)
            791 LOAD_CONST              14 (105)
            794 CALL_FUNCTION            1
            797 LOAD_GLOBAL              0 (chr)
            800 LOAD_CONST               9 (104)
            803 CALL_FUNCTION            1
            806 ROT_TWO             
            807 BINARY_ADD          
            808 ROT_TWO             
            809 BINARY_ADD          
            810 ROT_TWO             
            811 BINARY_ADD          
            812 LOAD_GLOBAL              0 (chr)
            815 LOAD_CONST              24 (78)
            818 CALL_FUNCTION            1
            821 LOAD_GLOBAL              0 (chr)
            824 LOAD_CONST              25 (123)
            827 CALL_FUNCTION            1
            830 LOAD_GLOBAL              0 (chr)
            833 LOAD_CONST              11 (110)
            836 CALL_FUNCTION            1
            839 LOAD_GLOBAL              0 (chr)
            842 LOAD_CONST              12 (111)
            845 CALL_FUNCTION            1
            848 ROT_TWO             
            849 BINARY_ADD          
            850 ROT_TWO             
            851 BINARY_ADD          
            852 ROT_TWO             
            853 BINARY_ADD          
            854 BINARY_ADD          
            855 LOAD_GLOBAL              0 (chr)
            858 LOAD_CONST               7 (121)
            861 CALL_FUNCTION            1
            864 LOAD_GLOBAL              0 (chr)
            867 LOAD_CONST               4 (32)
            870 CALL_FUNCTION            1
            873 LOAD_GLOBAL              0 (chr)
            876 LOAD_CONST              26 (119)
            879 CALL_FUNCTION            1
            882 LOAD_GLOBAL              0 (chr)
            885 LOAD_CONST              12 (111)
            888 CALL_FUNCTION            1
            891 ROT_TWO             
            892 BINARY_ADD          
            893 ROT_TWO             
            894 BINARY_ADD          
            895 ROT_TWO             
            896 BINARY_ADD          
            897 LOAD_GLOBAL              0 (chr)
            900 LOAD_CONST              17 (99)
            903 CALL_FUNCTION            1
            906 LOAD_GLOBAL              0 (chr)
            909 LOAD_CONST               4 (32)
            912 CALL_FUNCTION            1
            915 LOAD_GLOBAL              0 (chr)
            918 LOAD_CONST              16 (117)
            921 CALL_FUNCTION            1
            924 LOAD_GLOBAL              0 (chr)
            927 LOAD_CONST              12 (111)
            930 CALL_FUNCTION            1
            933 ROT_TWO             
            934 BINARY_ADD          
            935 ROT_TWO             
            936 BINARY_ADD          
            937 ROT_TWO             
            938 BINARY_ADD          
            939 BINARY_ADD          
            940 BINARY_ADD          
            941 LOAD_GLOBAL              0 (chr)
            944 LOAD_CONST              17 (99)
            947 CALL_FUNCTION            1
            950 LOAD_GLOBAL              0 (chr)
            953 LOAD_CONST               4 (32)
            956 CALL_FUNCTION            1
            959 LOAD_GLOBAL              0 (chr)
            962 LOAD_CONST              11 (110)
            965 CALL_FUNCTION            1
            968 LOAD_GLOBAL              0 (chr)
            971 LOAD_CONST               2 (97)
            974 CALL_FUNCTION            1
            977 ROT_TWO             
            978 BINARY_ADD          
            979 ROT_TWO             
            980 BINARY_ADD          
            981 ROT_TWO             
            982 BINARY_ADD          
            983 LOAD_GLOBAL              0 (chr)
            986 LOAD_CONST              14 (105)
            989 CALL_FUNCTION            1
            992 LOAD_GLOBAL              0 (chr)
            995 LOAD_CONST              20 (112)
            998 CALL_FUNCTION            1
           1001 LOAD_GLOBAL              0 (chr)
           1004 LOAD_CONST               6 (109)
           1007 CALL_FUNCTION            1
           1010 LOAD_GLOBAL              0 (chr)
           1013 LOAD_CONST              12 (111)
           1016 CALL_FUNCTION            1
           1019 ROT_TWO             
           1020 BINARY_ADD          
           1021 ROT_TWO             
           1022 BINARY_ADD          
           1023 ROT_TWO             
           1024 BINARY_ADD          
           1025 BINARY_ADD          
           1026 LOAD_GLOBAL              0 (chr)
           1029 LOAD_CONST               2 (97)
           1032 CALL_FUNCTION            1
           1035 LOAD_GLOBAL              0 (chr)
           1038 LOAD_CONST               4 (32)
           1041 CALL_FUNCTION            1
           1044 LOAD_GLOBAL              0 (chr)
           1047 LOAD_CONST               5 (101)
           1050 CALL_FUNCTION            1
           1053 LOAD_GLOBAL              0 (chr)
           1056 LOAD_CONST               1 (108)
           1059 CALL_FUNCTION            1
           1062 ROT_TWO             
           1063 BINARY_ADD          
           1064 ROT_TWO             
           1065 BINARY_ADD          
           1066 ROT_TWO             
           1067 BINARY_ADD          
           1068 LOAD_GLOBAL              0 (chr)
           1071 LOAD_CONST              22 (100)
           1074 CALL_FUNCTION            1
           1077 LOAD_GLOBAL              0 (chr)
           1080 LOAD_CONST              11 (110)
           1083 CALL_FUNCTION            1
           1086 ROT_TWO             
           1087 BINARY_ADD          
           1088 LOAD_GLOBAL              0 (chr)
           1091 LOAD_CONST              16 (117)
           1094 CALL_FUNCTION            1
           1097 LOAD_GLOBAL              0 (chr)
           1100 LOAD_CONST              13 (114)
           1103 CALL_FUNCTION            1
           1106 LOAD_GLOBAL              0 (chr)
           1109 LOAD_CONST               4 (32)
           1112 CALL_FUNCTION            1
           1115 ROT_TWO             
           1116 BINARY_ADD          
           1117 ROT_TWO             
           1118 BINARY_ADD          
           1119 BINARY_ADD          
           1120 BINARY_ADD          
           1121 BINARY_ADD          
           1122 BINARY_ADD          
           1123 LOAD_GLOBAL              0 (chr)
           1126 LOAD_CONST               7 (121)
           1129 CALL_FUNCTION            1
           1132 LOAD_GLOBAL              0 (chr)
           1135 LOAD_CONST               8 (80)
           1138 CALL_FUNCTION            1
           1141 LOAD_GLOBAL              0 (chr)
           1144 LOAD_CONST               4 (32)
           1147 CALL_FUNCTION            1
           1150 LOAD_GLOBAL              0 (chr)
           1153 LOAD_CONST              11 (110)
           1156 CALL_FUNCTION            1
           1159 ROT_TWO             
           1160 BINARY_ADD          
           1161 ROT_TWO             
           1162 BINARY_ADD          
           1163 ROT_TWO             
           1164 BINARY_ADD          
           1165 LOAD_GLOBAL              0 (chr)
           1168 LOAD_CONST              11 (110)
           1171 CALL_FUNCTION            1
           1174 LOAD_GLOBAL              0 (chr)
           1177 LOAD_CONST              12 (111)
           1180 CALL_FUNCTION            1
           1183 LOAD_GLOBAL              0 (chr)
           1186 LOAD_CONST               9 (104)
           1189 CALL_FUNCTION            1
           1192 LOAD_GLOBAL              0 (chr)
           1195 LOAD_CONST              10 (116)
           1198 CALL_FUNCTION            1
           1201 ROT_TWO             
           1202 BINARY_ADD          
           1203 ROT_TWO             
           1204 BINARY_ADD          
           1205 ROT_TWO             
           1206 BINARY_ADD          
           1207 BINARY_ADD          
           1208 LOAD_GLOBAL              0 (chr)
           1211 LOAD_CONST              10 (116)
           1214 CALL_FUNCTION            1
           1217 LOAD_GLOBAL              0 (chr)
           1220 LOAD_CONST               7 (121)
           1223 CALL_FUNCTION            1
           1226 LOAD_GLOBAL              0 (chr)
           1229 LOAD_CONST              21 (98)
           1232 CALL_FUNCTION            1
           1235 LOAD_GLOBAL              0 (chr)
           1238 LOAD_CONST               4 (32)
           1241 CALL_FUNCTION            1
           1244 ROT_TWO             
           1245 BINARY_ADD          
           1246 ROT_TWO             
           1247 BINARY_ADD          
           1248 ROT_TWO             
           1249 BINARY_ADD          
           1250 LOAD_GLOBAL              0 (chr)
           1253 LOAD_CONST              22 (100)
           1256 CALL_FUNCTION            1
           1259 LOAD_GLOBAL              0 (chr)
           1262 LOAD_CONST              12 (111)
           1265 CALL_FUNCTION            1
           1268 LOAD_GLOBAL              0 (chr)
           1271 LOAD_CONST              17 (99)
           1274 CALL_FUNCTION            1
           1277 LOAD_GLOBAL              0 (chr)
           1280 LOAD_CONST               5 (101)
           1283 CALL_FUNCTION            1
           1286 ROT_TWO             
           1287 BINARY_ADD          
           1288 ROT_TWO             
           1289 BINARY_ADD          
           1290 ROT_TWO             
           1291 BINARY_ADD          
           1292 BINARY_ADD          
           1293 BINARY_ADD          
           1294 LOAD_GLOBAL              0 (chr)
           1297 LOAD_CONST              11 (110)
           1300 CALL_FUNCTION            1
           1303 LOAD_GLOBAL              0 (chr)
           1306 LOAD_CONST              14 (105)
           1309 CALL_FUNCTION            1
           1312 LOAD_GLOBAL              0 (chr)
           1315 LOAD_CONST               4 (32)
           1318 CALL_FUNCTION            1
           1321 LOAD_GLOBAL              0 (chr)
           1324 LOAD_CONST               5 (101)
           1327 CALL_FUNCTION            1
           1330 ROT_TWO             
           1331 BINARY_ADD          
           1332 ROT_TWO             
           1333 BINARY_ADD          
           1334 ROT_TWO             
           1335 BINARY_ADD          
           1336 LOAD_GLOBAL              0 (chr)
           1339 LOAD_CONST              16 (117)
           1342 CALL_FUNCTION            1
           1345 LOAD_GLOBAL              0 (chr)
           1348 LOAD_CONST              12 (111)
           1351 CALL_FUNCTION            1
           1354 LOAD_GLOBAL              0 (chr)
           1357 LOAD_CONST               7 (121)
           1360 CALL_FUNCTION            1
           1363 LOAD_GLOBAL              0 (chr)
           1366 LOAD_CONST               4 (32)
           1369 CALL_FUNCTION            1
           1372 ROT_TWO             
           1373 BINARY_ADD          
           1374 ROT_TWO             
           1375 BINARY_ADD          
           1376 ROT_TWO             
           1377 BINARY_ADD          
           1378 BINARY_ADD          
           1379 LOAD_GLOBAL              0 (chr)
           1382 LOAD_CONST              13 (114)
           1385 CALL_FUNCTION            1
           1388 LOAD_GLOBAL              0 (chr)
           1391 LOAD_CONST              21 (98)
           1394 CALL_FUNCTION            1
           1397 LOAD_GLOBAL              0 (chr)
           1400 LOAD_CONST               4 (32)
           1403 CALL_FUNCTION            1
           1406 LOAD_GLOBAL              0 (chr)
           1409 LOAD_CONST              13 (114)
           1412 CALL_FUNCTION            1
           1415 ROT_TWO             
           1416 BINARY_ADD          
           1417 ROT_TWO             
           1418 BINARY_ADD          
           1419 ROT_TWO             
           1420 BINARY_ADD          
           1421 LOAD_GLOBAL              0 (chr)
           1424 LOAD_CONST              14 (105)
           1427 CALL_FUNCTION            1
           1430 LOAD_GLOBAL              0 (chr)
           1433 LOAD_CONST               2 (97)
           1436 CALL_FUNCTION            1
           1439 ROT_TWO             
           1440 BINARY_ADD          
           1441 LOAD_GLOBAL              0 (chr)
           1444 LOAD_CONST              27 (125)
           1447 CALL_FUNCTION            1
           1450 LOAD_GLOBAL              0 (chr)
           1453 LOAD_CONST              18 (33)
           1456 CALL_FUNCTION            1
           1459 LOAD_GLOBAL              0 (chr)
           1462 LOAD_CONST              11 (110)
           1465 CALL_FUNCTION            1
           1468 ROT_TWO             
           1469 BINARY_ADD          
           1470 ROT_TWO             
           1471 BINARY_ADD          
           1472 BINARY_ADD          
           1473 BINARY_ADD          
           1474 BINARY_ADD          
           1475 BINARY_ADD          
           1476 BINARY_ADD          
           1477 JUMP_ABSOLUTE         2212
        >> 1480 LOAD_GLOBAL              0 (chr)
           1483 LOAD_CONST               2 (97)
           1486 CALL_FUNCTION            1
           1489 LOAD_GLOBAL              0 (chr)
           1492 LOAD_CONST              20 (112)
           1495 CALL_FUNCTION            1
           1498 ROT_TWO             
           1499 BINARY_ADD          
           1500 LOAD_GLOBAL              0 (chr)
           1503 LOAD_CONST              26 (119)
           1506 CALL_FUNCTION            1
           1509 LOAD_GLOBAL              0 (chr)
           1512 LOAD_CONST              23 (115)
           1515 CALL_FUNCTION            1
           1518 LOAD_GLOBAL              0 (chr)
           1521 LOAD_CONST              23 (115)
           1524 CALL_FUNCTION            1
           1527 ROT_TWO             
           1528 BINARY_ADD          
           1529 ROT_TWO             
           1530 BINARY_ADD          
           1531 BINARY_ADD          
           1532 LOAD_GLOBAL              0 (chr)
           1535 LOAD_CONST              13 (114)
           1538 CALL_FUNCTION            1
           1541 LOAD_GLOBAL              0 (chr)
           1544 LOAD_CONST              12 (111)
           1547 CALL_FUNCTION            1
           1550 ROT_TWO             
           1551 BINARY_ADD          
           1552 LOAD_GLOBAL              0 (chr)
           1555 LOAD_CONST               4 (32)
           1558 CALL_FUNCTION            1
           1561 LOAD_GLOBAL              0 (chr)
           1564 LOAD_CONST              28 (58)
           1567 CALL_FUNCTION            1
           1570 LOAD_GLOBAL              0 (chr)
           1573 LOAD_CONST              22 (100)
           1576 CALL_FUNCTION            1
           1579 ROT_TWO             
           1580 BINARY_ADD          
           1581 ROT_TWO             
           1582 BINARY_ADD          
           1583 BINARY_ADD          
           1584 BINARY_ADD          
           1585 CALL_FUNCTION            1
           1588 JUMP_ABSOLUTE          750
        >> 1591 LOAD_GLOBAL              0 (chr)
           1594 LOAD_CONST              12 (111)
           1597 CALL_FUNCTION            1
           1600 LOAD_GLOBAL              0 (chr)
           1603 LOAD_CONST              13 (114)
           1606 CALL_FUNCTION            1
           1609 LOAD_GLOBAL              0 (chr)
           1612 LOAD_CONST              29 (87)
           1615 CALL_FUNCTION            1
           1618 ROT_TWO             
           1619 BINARY_ADD          
           1620 ROT_TWO             
           1621 BINARY_ADD          
           1622 LOAD_GLOBAL              0 (chr)
           1625 LOAD_CONST              20 (112)
           1628 CALL_FUNCTION            1
           1631 LOAD_GLOBAL              0 (chr)
           1634 LOAD_CONST               4 (32)
           1637 CALL_FUNCTION            1
           1640 LOAD_GLOBAL              0 (chr)
           1643 LOAD_CONST              30 (103)
           1646 CALL_FUNCTION            1
           1649 LOAD_GLOBAL              0 (chr)
           1652 LOAD_CONST              11 (110)
           1655 CALL_FUNCTION            1
           1658 ROT_TWO             
           1659 BINARY_ADD          
           1660 ROT_TWO             
           1661 BINARY_ADD          
           1662 ROT_TWO             
           1663 BINARY_ADD          
           1664 BINARY_ADD          
           1665 LOAD_GLOBAL              0 (chr)
           1668 LOAD_CONST              23 (115)
           1671 CALL_FUNCTION            1
           1674 LOAD_GLOBAL              0 (chr)
           1677 LOAD_CONST              23 (115)
           1680 CALL_FUNCTION            1
           1683 LOAD_GLOBAL              0 (chr)
           1686 LOAD_CONST               2 (97)
           1689 CALL_FUNCTION            1
           1692 ROT_TWO             
           1693 BINARY_ADD          
           1694 ROT_TWO             
           1695 BINARY_ADD          
           1696 LOAD_GLOBAL              0 (chr)
           1699 LOAD_CONST              22 (100)
           1702 CALL_FUNCTION            1
           1705 LOAD_GLOBAL              0 (chr)
           1708 LOAD_CONST              13 (114)
           1711 CALL_FUNCTION            1
           1714 LOAD_GLOBAL              0 (chr)
           1717 LOAD_CONST              12 (111)
           1720 CALL_FUNCTION            1
           1723 LOAD_GLOBAL              0 (chr)
           1726 LOAD_CONST              26 (119)
           1729 CALL_FUNCTION            1
           1732 ROT_TWO             
           1733 BINARY_ADD          
           1734 ROT_TWO             
           1735 BINARY_ADD          
           1736 ROT_TWO             
           1737 BINARY_ADD          
           1738 BINARY_ADD          
           1739 BINARY_ADD          
           1740 LOAD_GLOBAL              0 (chr)
           1743 LOAD_CONST              31 (46)
           1746 CALL_FUNCTION            1
           1749 LOAD_GLOBAL              0 (chr)
           1752 LOAD_CONST              31 (46)
           1755 CALL_FUNCTION            1
           1758 LOAD_GLOBAL              0 (chr)
           1761 LOAD_CONST              31 (46)
           1764 CALL_FUNCTION            1
           1767 ROT_TWO             
           1768 BINARY_ADD          
           1769 ROT_TWO             
           1770 BINARY_ADD          
           1771 LOAD_GLOBAL              0 (chr)
           1774 LOAD_CONST               5 (101)
           1777 CALL_FUNCTION            1
           1780 LOAD_GLOBAL              0 (chr)
           1783 LOAD_CONST               1 (108)
           1786 CALL_FUNCTION            1
           1789 LOAD_GLOBAL              0 (chr)
           1792 LOAD_CONST               8 (80)
           1795 CALL_FUNCTION            1
           1798 LOAD_GLOBAL              0 (chr)
           1801 LOAD_CONST               4 (32)
           1804 CALL_FUNCTION            1
           1807 ROT_TWO             
           1808 BINARY_ADD          
           1809 ROT_TWO             
           1810 BINARY_ADD          
           1811 ROT_TWO             
           1812 BINARY_ADD          
           1813 BINARY_ADD          
           1814 LOAD_GLOBAL              0 (chr)
           1817 LOAD_CONST               4 (32)
           1820 CALL_FUNCTION            1
           1823 LOAD_GLOBAL              0 (chr)
           1826 LOAD_CONST               5 (101)
           1829 CALL_FUNCTION            1
           1832 LOAD_GLOBAL              0 (chr)
           1835 LOAD_CONST              23 (115)
           1838 CALL_FUNCTION            1
           1841 LOAD_GLOBAL              0 (chr)
           1844 LOAD_CONST               2 (97)
           1847 CALL_FUNCTION            1
           1850 ROT_TWO             
           1851 BINARY_ADD          
           1852 ROT_TWO             
           1853 BINARY_ADD          
           1854 ROT_TWO             
           1855 BINARY_ADD          
           1856 LOAD_GLOBAL              0 (chr)
           1859 LOAD_CONST               4 (32)
           1862 CALL_FUNCTION            1
           1865 LOAD_GLOBAL              0 (chr)
           1868 LOAD_CONST               7 (121)
           1871 CALL_FUNCTION            1
           1874 LOAD_GLOBAL              0 (chr)
           1877 LOAD_CONST              13 (114)
           1880 CALL_FUNCTION            1
           1883 LOAD_GLOBAL              0 (chr)
           1886 LOAD_CONST              10 (116)
           1889 CALL_FUNCTION            1
           1892 ROT_TWO             
           1893 BINARY_ADD          
           1894 ROT_TWO             
           1895 BINARY_ADD          
           1896 ROT_TWO             
           1897 BINARY_ADD          
           1898 BINARY_ADD          
           1899 BINARY_ADD          
           1900 BINARY_ADD          
           1901 LOAD_GLOBAL              0 (chr)
           1904 LOAD_CONST               2 (97)
           1907 CALL_FUNCTION            1
           1910 LOAD_GLOBAL              0 (chr)
           1913 LOAD_CONST              30 (103)
           1916 CALL_FUNCTION            1
           1919 LOAD_GLOBAL              0 (chr)
           1922 LOAD_CONST               2 (97)
           1925 CALL_FUNCTION            1
           1928 ROT_TWO             
           1929 BINARY_ADD          
           1930 ROT_TWO             
           1931 BINARY_ADD          
           1932 LOAD_GLOBAL              0 (chr)
           1935 LOAD_CONST               4 (32)
           1938 CALL_FUNCTION            1
           1941 LOAD_GLOBAL              0 (chr)
           1944 LOAD_CONST              31 (46)
           1947 CALL_FUNCTION            1
           1950 LOAD_GLOBAL              0 (chr)
           1953 LOAD_CONST              11 (110)
           1956 CALL_FUNCTION            1
           1959 LOAD_GLOBAL              0 (chr)
           1962 LOAD_CONST              14 (105)
           1965 CALL_FUNCTION            1
           1968 ROT_TWO             
           1969 BINARY_ADD          
           1970 ROT_TWO             
           1971 BINARY_ADD          
           1972 ROT_TWO             
           1973 BINARY_ADD          
           1974 BINARY_ADD          
           1975 LOAD_GLOBAL              0 (chr)
           1978 LOAD_CONST               4 (32)
           1981 CALL_FUNCTION            1
           1984 LOAD_GLOBAL              0 (chr)
           1987 LOAD_CONST              12 (111)
           1990 CALL_FUNCTION            1
           1993 LOAD_GLOBAL              0 (chr)
           1996 LOAD_CONST              32 (68)
           1999 CALL_FUNCTION            1
           2002 ROT_TWO             
           2003 BINARY_ADD          
           2004 ROT_TWO             
           2005 BINARY_ADD          
           2006 LOAD_GLOBAL              0 (chr)
           2009 LOAD_CONST               4 (32)
           2012 CALL_FUNCTION            1
           2015 LOAD_GLOBAL              0 (chr)
           2018 LOAD_CONST              10 (116)
           2021 CALL_FUNCTION            1
           2024 LOAD_GLOBAL              0 (chr)
           2027 LOAD_CONST              12 (111)
           2030 CALL_FUNCTION            1
           2033 LOAD_GLOBAL              0 (chr)
           2036 LOAD_CONST              11 (110)
           2039 CALL_FUNCTION            1
           2042 ROT_TWO             
           2043 BINARY_ADD          
           2044 ROT_TWO             
           2045 BINARY_ADD          
           2046 ROT_TWO             
           2047 BINARY_ADD          
           2048 BINARY_ADD          
           2049 BINARY_ADD          
           2050 LOAD_GLOBAL              0 (chr)
           2053 LOAD_CONST              16 (117)
           2056 CALL_FUNCTION            1
           2059 LOAD_GLOBAL              0 (chr)
           2062 LOAD_CONST              13 (114)
           2065 CALL_FUNCTION            1
           2068 LOAD_GLOBAL              0 (chr)
           2071 LOAD_CONST              21 (98)
           2074 CALL_FUNCTION            1
           2077 ROT_TWO             
           2078 BINARY_ADD          
           2079 ROT_TWO             
           2080 BINARY_ADD          
           2081 LOAD_GLOBAL              0 (chr)
           2084 LOAD_CONST              33 (102)
           2087 CALL_FUNCTION            1
           2090 LOAD_GLOBAL              0 (chr)
           2093 LOAD_CONST               4 (32)
           2096 CALL_FUNCTION            1
           2099 LOAD_GLOBAL              0 (chr)
           2102 LOAD_CONST               5 (101)
           2105 CALL_FUNCTION            1
           2108 LOAD_GLOBAL              0 (chr)
           2111 LOAD_CONST              10 (116)
           2114 CALL_FUNCTION            1
           2117 ROT_TWO             
           2118 BINARY_ADD          
           2119 ROT_TWO             
           2120 BINARY_ADD          
           2121 ROT_TWO             
           2122 BINARY_ADD          
           2123 BINARY_ADD          
           2124 LOAD_GLOBAL              0 (chr)
           2127 LOAD_CONST               5 (101)
           2130 CALL_FUNCTION            1
           2133 LOAD_GLOBAL              0 (chr)
           2136 LOAD_CONST              17 (99)
           2139 CALL_FUNCTION            1
           2142 LOAD_GLOBAL              0 (chr)
           2145 LOAD_CONST              13 (114)
           2148 CALL_FUNCTION            1
           2151 LOAD_GLOBAL              0 (chr)
           2154 LOAD_CONST              12 (111)
           2157 CALL_FUNCTION            1
           2160 ROT_TWO             
           2161 BINARY_ADD          
           2162 ROT_TWO             
           2163 BINARY_ADD          
           2164 ROT_TWO             
           2165 BINARY_ADD          
           2166 LOAD_GLOBAL              0 (chr)
           2169 LOAD_CONST              34 (41)
           2172 CALL_FUNCTION            1
           2175 LOAD_GLOBAL              0 (chr)
           2178 LOAD_CONST              35 (61)
           2181 CALL_FUNCTION            1
           2184 LOAD_GLOBAL              0 (chr)
           2187 LOAD_CONST               4 (32)
           2190 CALL_FUNCTION            1
           2193 LOAD_GLOBAL              0 (chr)
           2196 LOAD_CONST              31 (46)
           2199 CALL_FUNCTION            1
           2202 ROT_TWO             
           2203 BINARY_ADD          
           2204 ROT_TWO             
           2205 BINARY_ADD          
           2206 ROT_TWO             
           2207 BINARY_ADD          
           2208 BINARY_ADD          
           2209 BINARY_ADD          
           2210 BINARY_ADD          
           2211 BINARY_ADD          
        >> 2212 PRINT_ITEM          
           2213 PRINT_NEWLINE       
           2214 LOAD_CONST               0 (None)
           2217 RETURN_VALUE        
