import numpy as np

GP = np.array([0.99,
3.7,
6.1,
8.6,
11.2,
13.6,
16.1,
18.7,
21.1,
23.8,
26.3,
28.7,
31.2,
33.7,
36.1,
38.6,
41.2,
43.6,
46.1,
48.5,
51.2,
53.5,
55.9,
58.4,
61.1,
63.9,
66.5,
69.1,
71.7,
74.5,
77.3,
79.8,
82.6,
85.3,
88.1,
90.9,
93.7,
96.3,
99.1,
101.8,
104.6,
107.1,
109.8,
112.3,
114.9,
117.5,
120.2,
122.7,
125.3,
127.8,
130.4,
133.1,
135.9,
138.5,
141.1,
143.8,
146.6,
149.3,
152.1,
154.8,
157.4,
160.1,
162.7,
165.4,
168.1,
170.1,
172.6,
175.2,
177.9,
180.7,
183.3,
186.1,
188.8,
191.4,
194.1,
196.9,
199.6,
202.4,
205.1,
207.7,
210.3,
212.9,
215.6,
218.3,
220.8,
223.2,
225.6,
227.9,
230.2,
232.4,
234.6,
236.7,
238.8,
240.7,
242.7,
244.5,
246.3,
248.1,
249.7,
251.4
])
GD = np.array([0.4,
1.3,
2.1,
3.1,
4.1,
5.1,
6.1,
6.3,
7.4,
8.6,
9.8,
11.1,
12.3,
13.6,
15,
16.3,
17.8,
19.2,
20.6,
22.2,
23.7,
25.3,
26.9,
28.5,
30.2,
31.9,
33.6,
35.3,
37.1,
38.8,
40.6,
42.4,
44.2,
46.1,
48,
49.9,
51.8,
53.7,
55.6,
57.6,
59.6,
61.7,
63.8,
65.9,
68.1,
70.3,
72.5,
74.8,
77.1,
79.5,
81.9,
84.2,
86.5,
88.8,
91.2,
93.7,
96.2,
98.8,
101.3,
104,
106.5,
109.3,
112,
114.9,
117.8,
120.6,
123.4,
126.2,
129,
131.9,
134.8,
137.6,
140.5,
143.5,
146.3,
149.1,
152,
155,
157.8,
160.7,
163.6,
166.5,
169.5,
172.4,
175.3,
178.2,
181.1,
183.9,
186.8,
189.8,
192.8,
195.9,
199,
202.4,
206.3,
210.8,
216.3,
223.3,
232,
242.9])
GPmax = max(GP)
GPmin = min(GP)
GDmax = max(GD)
GDmin = min(GD)

GP_new = np.array([(each - GPmin) / (GPmax - GPmin) for each in GP])
GD_new = np.array([(each - GDmin) / (GDmax - GDmin) for each in GD])