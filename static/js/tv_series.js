



function mouseover(id){

      var tv=document.getElementsByClassName("tv_poster");
      if(document.getElementById(id).style.display==="none"){
          tv[id-1].style.display="none";

          tv[id-1].style.border="10px solid #EA2027";
          document.getElementById(id).style.display="";



          window.scrollBy(0,300);
      }
      else{
          tv[id-1].style.display="";
          tv[id-1].style.border="";
          document.getElementById(id).style.display="none";


      }



}

function show(id){
      if(document.getElementById(id).style.display="none"){
          document.getElementById(id).style.display="";

          window.scrollBy(0,300);
      }
      else{
         document.getElementById(id).style.display="none";


      }


}