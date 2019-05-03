function show(id){
      if(document.getElementById(id).style.display==="none"){
          document.getElementById(id).style.display="inline-block";

          window.scrollBy(0,300);
      }
      else{
         document.getElementById(id).style.display="none";


      }


}