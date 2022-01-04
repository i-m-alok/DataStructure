<h2><a href="https://leetcode.com/problems/k-th-symbol-in-grammar/">779. K-th Symbol in Grammar</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">We build a table of <code style="user-select: auto;">n</code> rows (<strong style="user-select: auto;">1-indexed</strong>). We start by writing <code style="user-select: auto;">0</code> in the <code style="user-select: auto;">1<sup style="user-select: auto;">st</sup></code> row. Now in every subsequent row, we look at the previous row and replace each occurrence of <code style="user-select: auto;">0</code> with <code style="user-select: auto;">01</code>, and each occurrence of <code style="user-select: auto;">1</code> with <code style="user-select: auto;">10</code>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, for <code style="user-select: auto;">n = 3</code>, the <code style="user-select: auto;">1<sup style="user-select: auto;">st</sup></code> row is <code style="user-select: auto;">0</code>, the <code style="user-select: auto;">2<sup style="user-select: auto;">nd</sup></code> row is <code style="user-select: auto;">01</code>, and the <code style="user-select: auto;">3<sup style="user-select: auto;">rd</sup></code> row is <code style="user-select: auto;">0110</code>.</li>
</ul>

<p style="user-select: auto;">Given two integer <code style="user-select: auto;">n</code> and <code style="user-select: auto;">k</code>, return the <code style="user-select: auto;">k<sup style="user-select: auto;">th</sup></code> (<strong style="user-select: auto;">1-indexed</strong>) symbol in the <code style="user-select: auto;">n<sup style="user-select: auto;">th</sup></code> row of a table of <code style="user-select: auto;">n</code> rows.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 1, k = 1
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> row 1: <u style="user-select: auto;">0</u>
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 2, k = 1
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> 
row 1: 0
row 2: <u style="user-select: auto;">0</u>1
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 2, k = 2
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> 
row 1: 0
row 2: 0<u style="user-select: auto;">1</u>
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 30</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 2<sup style="user-select: auto;">n - 1</sup></code></li>
</ul>
</div>