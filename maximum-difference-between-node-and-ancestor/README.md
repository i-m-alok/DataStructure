<h2>1026. Maximum Difference Between Node and Ancestor</h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">root</code> of a binary tree, find the maximum value <code style="user-select: auto;">v</code> for which there exist <strong style="user-select: auto;">different</strong> nodes <code style="user-select: auto;">a</code> and <code style="user-select: auto;">b</code> where <code style="user-select: auto;">v = |a.val - b.val|</code> and <code style="user-select: auto;">a</code> is an ancestor of <code style="user-select: auto;">b</code>.</p>

<p style="user-select: auto;">A node <code style="user-select: auto;">a</code> is an ancestor of <code style="user-select: auto;">b</code> if either: any child of <code style="user-select: auto;">a</code> is equal to <code style="user-select: auto;">b</code>&nbsp;or any child of <code style="user-select: auto;">a</code> is an ancestor of <code style="user-select: auto;">b</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg" style="width: 400px; height: 390px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [8,3,10,1,6,null,14,null,null,4,7,13]
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation: </strong>We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg" style="width: 250px; height: 349px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,2,null,0,3]
<strong style="user-select: auto;">Output:</strong> 3
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[2, 5000]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>