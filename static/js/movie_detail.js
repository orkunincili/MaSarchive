function others(){
     if(document.getElementById("others").style.display==="none"){
         document.getElementById("others").style.display="";

     }
     else{
         document.getElementById("others").style.display="none";
     }
}
function note_form(){
     if(document.getElementById("note_form").style.display==="none"){
        document.getElementById("note_form").style.display="";
        document.getElementById("movie_notes").style.display="none";
        document.getElementById("id_notes").style.height="225px";
        document.getElementById("id_notes").style.width="99.50%";
        document.getElementById("id_notes").style.color="rgba(255,255,255,0.7)";
        document.getElementById("id_notes").style.backgroundColor="rgb(0,0,0,0)";
        document.getElementById("id_notes").style.border="1px solid rgba(0,0,0,0)";

     }
     else{
        document.getElementById("note_form").style.display="none";
        document.getElementById("movie_notes").style.display="";
     }

}

