import pandas as pd
questions = pd.read_csv('questions.csv')

print '''<!DOCTYPE html>
<meta charset="utf-8">
<style>



body {
  font-family: "Raleway",  sans-serif;
  margin: auto;
  position: relative;
  width: 960px;
  font-size: 1.2em;
}
</style>
<html> 
  <head> 
    <link href='http://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
    <title>Statistical Compass Questionnaire</title> 
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  </head> 
<body>
<h1> Statistical Compass Questionnaire</h1>
<h2>Enter a response from -2 (strongly disagree) to +2 (strongly agree):</h2>
<form action="#" method="">
<div data-role="fieldcontain">
'''
#print 
nq=len(questions.iloc[:])
#print nq
for i in range(0, questions.shape[0]):
     
     st="%f %f %f"%(questions.iloc[i, 1],questions.iloc[i, 2],questions.iloc[i, 3])
     #print st
     print questions.iloc[i, 0],'''
<br>
-2
<input class="calc" type="radio" name="radio%d" value="-2 %s">
-1                                                          
<input class="calc" type="radio" name="radio%d" value="-1 %s">
0                                                           
<input class="calc" type="radio" name="radio%d" value="0 %s">
1                                                           
<input class="calc" type="radio" name="radio%d" value="1 %s">
2                                                           
<input class="calc" type="radio" name="radio%d" value="2 %s">
</p>


'''%(i,st,i,st,i,st,i,st,i,st)

print '''


<input type="submit" name="sum" onclick="displayscore();"> 
</div>      
</form>
<script>
var score = new Array(3);
for (i=1; i<=3; i++){score[i]=0};
function displayscore(){
	console.log("here");
	alert("Your position in 3D is "+ score);
}
function calcscore() {
    
    $(".calc:checked").each(function() {
        console.log($(this).val(), +$(this).val().split(" ")[0]);
        for (i=1; i<=3; i++)
	   {
	   score[i] += +($(this).val().split(" ")[i])*parseInt($(this).val().split(" ")[0], 10);
	   console.log("here",score);
			
	   }
    console.log(score[1]);

//$("input[name=sum]").val(score);

})};
$().ready(function() {
    $(".calc").change(function() {
        calcscore()
    });
});
</script>
</body>
</html>
'''

