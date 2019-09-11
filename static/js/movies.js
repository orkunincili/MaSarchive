var movies_json = '{{ movies_json|escapejs }}';
document.getElementById("demo").innerHTML = movies_json;
function note_form(){
     if(document.getElementById("note_form").style.display==="none"){
        document.getElementById("note_form").style.display="";
        document.getElementById("movie_notes").style.display="none";
        document.getElementById("id_notes").style.height="225px";
        document.getElementById("id_notes").style.width="99.50%";
        document.getElementById("id_notes").style.color="rgba(255,255,255,0.7)";
        document.getElementById("id_notes").style.backgroundColor="rgba(0,0,0,0.30)";
        document.getElementById("id_notes").style.border="1px solid rgba(0,0,0,0.90)";

     }
     else{
        document.getElementById("note_form").style.display="none";
        document.getElementById("movie_notes").style.display="";
     }

}

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

    getElementById("see_notes").style.display=="";

}
function see_more_out(){
    var movie_content=document.getElementsByClassName("movie_content");


    getElementById("see_notes").style.display="none";




}

function note_form(){
     var note=document.getElementsByClassName("note_form");
     note[0].style.display="";
}

