<h2>1015. Smallest Integer Divisible by K</h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a positive integer <code style="user-select: auto;">k</code>, you need to find the <strong style="user-select: auto;">length</strong> of the <strong style="user-select: auto;">smallest</strong> positive integer <code style="user-select: auto;">n</code> such that <code style="user-select: auto;">n</code> is divisible by <code style="user-select: auto;">k</code>, and <code style="user-select: auto;">n</code> only contains the digit <code style="user-select: auto;">1</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">length</strong> of </em><code style="user-select: auto;">n</code>. If there is no such <code style="user-select: auto;">n</code>, return -1.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Note:</strong> <code style="user-select: auto;">n</code> may not fit in a 64-bit signed integer.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> k = 1
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> The smallest answer is n = 1, which has length 1.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> k = 2
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> There is no such positive integer n divisible by 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> k = 3
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> The smallest answer is n = 111, which has length 3.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>