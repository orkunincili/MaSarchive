



function mouseover(id){

      var movie=document.getElementsByClassName("movie_poster");
      if(document.getElementById(id).style.display==="none"){
          movie[id-1].style.display="none";

          movie[id-1].style.border="10px solid #EA2027";
          document.getElementById(id).style.display="";



          window.scrollBy(0,300);
      }
      else{
          movie[id-1].style.display="";
          movie[id-1].style.border="";
          document.getElementById(id).style.display="none";


      }



}
function see_more_on(){
    var movie_content=document.getElementsByClassName("movie_content");
     movie_content[id-1]
    getElementById("see_notes").style.display=="";

}
function see_more_out(){
    var movie_content=document.getElementsByClassName("movie_content");


    getElementById("see_notes").style.display="none";




}

