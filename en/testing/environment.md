On an x8664 architecture / 32 core hyperthread CPUU E5-2630 v3 @ 2.40 GHz CPUU 2356K L2 Cache20MB L3 Cache1 128G memory and a 500GB SSD machine we compared the Redishrer level DBN DezhouKV and Sogou-QDB.
<table border="1">
  <tr>
    <th>DB</th>
     <th>Method</th>
    <th>percent returned</th>
   <th>cost</th>
  </tr>
 <tbody><tr height="18" style="height:13.5pt">
  <td height="18" width="68" style="height:13.5pt">Redis</td>
  <td width="36" style="width:27pt">SET</td>
  <td class="xl65" align="right" width="68" style="width:51pt">17.93%</td>
  <td width="129" style="width:97pt">1 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">Redis</td>
  <td>SET</td>
  <td class="xl65" align="right">94.57%</td>
  <td>2 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">Redis</td>
  <td>SET</td>
  <td class="xl65" align="right">99.45%</td>
  <td>3 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">Redis</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>3 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" colspan="4" style="height:13.5pt;mso-ignore:colspan"></td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">Redis</td>
  <td>GET</td>
  <td class="xl65" align="right">91.77%</td>
  <td>1 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">Redis</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>1 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" colspan="4" style="height:13.5pt;mso-ignore:colspan"></td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>SET</td>
  <td class="xl65" align="right">0.01%</td>
  <td>1 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>SET</td>
  <td class="xl65" align="right">0.09%</td>
  <td>2 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>SET</td>
  <td class="xl65" align="right">33.69%</td>
  <td>3 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>SET</td>
  <td class="xl65" align="right">97.61%</td>
  <td>4 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>4 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" colspan="4" style="height:13.5pt;mso-ignore:colspan"></td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>GET</td>
  <td class="xl65" align="right">0.49%</td>
  <td>1 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>GET</td>
  <td class="xl65" align="right">99.61%</td>
  <td>2 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">LevelDB</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>2 milliseconds</td>
 </tr> </tbody>
</table>    
Table：For Redis 10000 requests has a SET-QPS of 270270.28, and GET-QPS of 454545.47, For LevelDB, SET-QPS 119047.62 and GET-QPS 232558.12.
<table border="1">
  <tr>
    <th>DezhouKV processes</th>
    <th>Method</th>
    <th>percent returned</th>
   <th>cost</th>
 </tr>
 <tbody><tr height="18" style="height:13.5pt">
  <td height="18" width="52" style="height:13.5pt;width:39pt">1+1+0</td>
  <td width="36" style="width:27pt">SET</td>
  <td class="xl65" align="right" width="68" style="width:51pt">0.00%</td>
  <td width="138" style="width:104pt">9 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>10 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">0.67%</td>
  <td>11 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">28.64%</td>
  <td>12 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">46.79%</td>
  <td>13 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">60.67%</td>
  <td>14 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">73.93%</td>
  <td>15 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">84.73%</td>
  <td>16 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">91.27%</td>
  <td>17 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">95.14%</td>
  <td>18 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">97.43%</td>
  <td>19 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">98.72%</td>
  <td>20 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.40%</td>
  <td>21 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.66%</td>
  <td>22 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.81%</td>
  <td>23 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.89%</td>
  <td>24 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.92%</td>
  <td>25 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.95%</td>
  <td>26 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.97%</td>
  <td>27 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.97%</td>
  <td>28 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.98%</td>
  <td>29 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>30 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>31 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>32 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>33 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>34 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>34 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" colspan="2" style="height:13.5pt;mso-ignore:colspan"></td>
  <td class="xl65"></td>
  <td></td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>5 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>8 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>9 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>11 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.81%</td>
  <td>12 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">21.65%</td>
  <td>13 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">38.37%</td>
  <td>14 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">51.94%</td>
  <td>15 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">64.84%</td>
  <td>16 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">76.72%</td>
  <td>17 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">85.43%</td>
  <td>18 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">90.79%</td>
  <td>19 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">94.80%</td>
  <td>20 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">97.32%</td>
  <td>21 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">98.69%</td>
  <td>22 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.29%</td>
  <td>23 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.58%</td>
  <td>24 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.71%</td>
  <td>25 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.79%</td>
  <td>26 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.83%</td>
  <td>27 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.88%</td>
  <td>28 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.90%</td>
  <td>29 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.94%</td>
  <td>30 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.95%</td>
  <td>31 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.96%</td>
  <td>32 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.97%</td>
  <td>33 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.98%</td>
  <td>34 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>35 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>36 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>37 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>38 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">1+1+0</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>38 milliseconds</td>
 </tr>
 <tr height="36" style="height:27.0pt;mso-xlrowspan:2">
  <td height="36" colspan="4" style="height:27.0pt;mso-ignore:colspan"></td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>2 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>3 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>4 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">5.13%</td>
  <td>5 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">46.15%</td>
  <td>6 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">71.92%</td>
  <td>7 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">83.62%</td>
  <td>8 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">91.15%</td>
  <td>9 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">94.56%</td>
  <td>10 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">95.90%</td>
  <td>11 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">96.68%</td>
  <td>12 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">97.51%</td>
  <td>13 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">98.39%</td>
  <td>14 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.10%</td>
  <td>15 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.58%</td>
  <td>16 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.81%</td>
  <td>17 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.93%</td>
  <td>18 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>19 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>20 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>21 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>SET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>21 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" colspan="4" style="height:13.5pt;mso-ignore:colspan"></td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>2 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>3 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.00%</td>
  <td>4 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">0.36%</td>
  <td>5 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">22.62%</td>
  <td>6 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">53.66%</td>
  <td>7 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">67.99%</td>
  <td>8 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">78.18%</td>
  <td>9 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">85.70%</td>
  <td>10 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">90.25%</td>
  <td>11 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">92.83%</td>
  <td>12 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">94.62%</td>
  <td>13 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">96.08%</td>
  <td>14 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">97.24%</td>
  <td>15 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">98.23%</td>
  <td>16 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">98.95%</td>
  <td>17 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.44%</td>
  <td>18 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.77%</td>
  <td>19 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.91%</td>
  <td>20 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.97%</td>
  <td>21 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">99.99%</td>
  <td>22 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>23 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>24 milliseconds</td>
 </tr>
 <tr height="18" style="height:13.5pt">
  <td height="18" style="height:13.5pt">4+4+0</td>
  <td>GET</td>
  <td class="xl65" align="right">100.00%</td>
  <td>24 milliseconds</td>
 </tr>
</tbody>
</table>    
Table：For DezhouKV processes, it means use how many processes for (DRAM\SSD\HDD), for 1+1+0, it uses 1 DRAMory process and 1 ssd process and no hdd process, thus data for hdd are stored in ssd backend(s). DezhouKV-1 process SET-QPS 28966.70, and GET-QPS 26009.36. DezhouKV-4 process SET-QPS 59174.05, and GET-QPS 51280.47.