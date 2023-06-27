# Sequence Alignment

Semester: <b>4<br></b>
Subject: <b>Design and Analysis of Algorithms</b><br>
Examination: <b>CIA 1</b><br>
Time: <b>90 minutes</b><br>

<hr>

 <h3><u>CONTENTS:</u></h3>
 <ol type="I">
	<li>Objectives</li>
  	<li>Code Output</li>
   	<li>Time Complexity</li>
    	<li>Space Complexity</li>
 </ol>

 <hr>
	 
<h3><u>OBJECTIVES:</u></h3>
 1) Functions to generate randomised 16-character sequences 's1' & 's2' using given character set - Done.<br>
 2) Recursive function calls are encouraged - Noted.<br>
 3) Output: First 4 maximal score sub-sequences - Done.<br>
 4) Space Complexity - Done.<br>
 5) Time Complexity - Done.<br>
 6) Generate Alignment Matrix - Done.<br>
 7) Traceback in Alignment Matrix - Done.<br>
 8) Alignment Scores - Done.<br>
<br>
[
TODO:
Automate Step 3, to provide 'n' top-scoring sequences
]

<hr>

<h3><u>CODE OUTPUT:</u></h3><br>
<img width="432" alt="Screenshot 2023-06-27 at 21 13 16" src="https://github.com/SheriffAbdullah/alignment-problem/assets/94511829/8d7ff0d3-9b90-4c75-ab19-66f31fc28988">
<br>
<img width="432" alt="Screenshot 2023-06-27 at 21 13 37" src="https://github.com/SheriffAbdullah/alignment-problem/assets/94511829/b7398836-e950-4e74-a578-bab518766392">

<br><hr>

<h3><u>TIME COMPLEXITY:</u></h3>
<br>
<table>
	<tr>
		<th>Section</th>
		<th>Time Complexity</th>	
		<th>Explanation</th>
  	</tr>
  	<tr>
    	<td>Randomised Sequence Generation</td>
    	<td align="center">O(n)</td>
    	<td>Depends linearly on the length of the character set. </td>
  	</tr>
  	<tr>
    	<td>Alignment Matrix Initialisation</td>
    	<td align="center">O(l1 * l2)</td>
    	<td>Initialises an alignment matrix of size '(l2 + 1) * (l1 + 1)'.</td>
  	</tr>
  	<tr>
    	<td>Recursive Alignment Matrix Generation <br>[dp]</td>
    	<td align="center">O(l1 * l2)</td>
    	<td>The recursive function 'dp' is called for each cell of the alignment matrix, resulting in a total of '(l1 + 1) * (l2 + 1)' function calls. Each function call performs constant time operations - comparisons, assignments, and recursive calls, leading to a time complexity proportional to the product of the string lengths.</td>
	</tr>
  	<tr>
    	<td>Traceback in Alignment Matrix <br>[tracepath]</td>
    	<td align="center">O(l1 + l2)</td>
    	<td>The traceback process stops when reaching a cell with a score of '0', which occurs in the worst case when all cells are filled with values greater than '0'. The longest resultant sequence in the matrix is of length 'l1 + l2'.</td>
  	</tr>
 	<tr>
  		<td colspan="3"><i>'n' = size of the character set.<br>'l1' & 'l2' = lengths of sequences 's1' & 's2', respectively.</i></td>
 	</tr>
</table>

<br><hr>

<h3><u>SPACE COMPLEXITY:</u></h3>
<br>
<table>
	<tr>
		<th>Section</th>
		<th>Space Complexity</th>	
		<th>Explanation</th>
  	</tr>
	<tr>
    	<td>Input Sequences</td>
    	<td align="center">O(l1 + l2)</td>
    	<td>The space required to store the input sequences is proportional to the lengths of 's1' and 's2', respectively.</td>
  	</tr>
  	<tr>
    	<td>Alignment Matrix</td>
    	<td align="center">O(l1 * l2)</td>
    	<td>The alignment matrix has dimensions '(l2 + 1) * (l1 + 1)'.</td>
  	</tr>
   <tr>
    	<td>Recursive Calls</td>
    	<td align="center">-</td>
    	<td>The recursive calls in the 'dp' and 'tracepath' functions do not require additional space for each call since the function parameters and local variables are stored on the stack. </td>
  	</tr>
  	<tr>
  		<td colspan="3"><i>'l1' & 'l2' = lengths of sequences 's1' & 's2', respectively.</i></td>
 	</tr>
</table>


