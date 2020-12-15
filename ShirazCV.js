var aboutMeContent= "I am a motivated worker with natural leadership skills. <br>I think both analytically and strategically.<br> I have given large responsibilities and worked under pressure."; 

var education1="BA in Information System Management | 2018-Present | Ben Gurion University <br> <ui> <li>Currently at the third year </li>  <li>Throughout my degree I have volunteered with 'Perach'.</li> <li>I have volunteered and tutored adults with special needs.</li><li>GPA:89</li>  "; 
var education2="<br> Amal Lady Davis High School | 2007-2013 <br> <ui> <li>Majored in Literature and Film.</li> <li>Graduated with High honors.</li>";
var experiance="Salesforce analyst|2019-Present|Ben Gurion University,international affairs.<br><br> <ui> <li>Responsible for operating the system in code, Forms, Business processes, etc.</li> <li>Providing first hand assistance to users who encountered technical difficulties.</li><li>Characterization of business processes and their implantation in the system.</li>";

function mouseOver() {
    document.getElementById("contactme").style.backgroundColor="silver";

  }
  
  function mouseOut() {
    document.getElementById("contactme").style.backgroundColor="rgb(233, 193, 227)"; 
   
  }

  function changeToAboutMe(){
   document.getElementById("conpar").innerHTML= aboutMeContent;
   document.getElementById("about").style.backgroundColor="rgb(226, 67, 173)";
   document.getElementById("home").style.backgroundColor="rgb(233, 193, 227)";
   document.getElementById("education").style.backgroundColor="rgb(233, 193, 227)";
   document.getElementById("profsessional").style.backgroundColor="rgb(233, 193, 227)";
   document.getElementById("home").onmouseover.style.backgroundColor="white";

  }
  function changeToEducation(){
    document.getElementById("mainheader").innerHTML= "My Education";
    document.getElementById("conpar").innerHTML= education1+ education2;
    document.getElementById("education").style.backgroundColor="rgb(226, 67, 173)";
    document.getElementById("home").style.backgroundColor="rgb(233, 193, 227)";
    document.getElementById("about").style.backgroundColor="rgb(233, 193, 227)";
    document.getElementById("profsessional").style.backgroundColor="rgb(233, 193, 227)";

   }

   function changeToExperiance(){
    document.getElementById("mainheader").innerHTML= "My Experiance";
    document.getElementById("conpar").innerHTML= experiance;
    document.getElementById("profsessional").style.backgroundColor="rgb(226, 67, 173)";
    document.getElementById("home").style.backgroundColor="rgb(233, 193, 227)";
    document.getElementById("about").style.backgroundColor="rgb(233, 193, 227)";
    document.getElementById("education").style.backgroundColor="rgb(233, 193, 227)";
   }


 

 

   