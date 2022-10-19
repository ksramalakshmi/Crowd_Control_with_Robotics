document.querySelector("#a").onclick = function(){
  
  eel.entry_excel(2)(
    function(i){
      if (i == 1)
      {var p = document.getElementById('indi');
      p.innerHTML = "Ticketing successful for Mysore Road"}
      else
      {var p = document.getElementById('indi');
      p.innerHTML = "Seats full"}
    }
  )
}

document.querySelector("#b").onclick = function(){
  
  eel.entry_excel(3)(
    function(){
      var p = document.getElementById('indi');
      p.innerHTML = "Ticketing successful for Deepanjali Nagar"
    }
  )
}

document.querySelector("#c").onclick = function(){
  
  eel.entry_excel(4)(
    function(){
      var p = document.getElementById('indi');
      p.innerHTML = "Ticketing successful for Attiguppe"
    }
  )
}

document.querySelector("#d").onclick = function(){
  
  eel.entry_excel(5)(
    function(){
      var p = document.getElementById('indi');
      p.innerHTML = "Ticketing successful for Vijayanagar"
    }
  )
}

document.querySelector("#e").onclick = function(){
  
  eel.entry_excel(6)(
    function(){
      var p = document.getElementById('indi');
      p.innerHTML = "Ticketing successful for Hosahalli"
    }
  )
}

document.querySelector("#f").onclick = function(){
  
  eel.entry_excel(7)(
    function(){
      var p = document.getElementById('indi');
      p.innerHTML = "Ticketing successful for Magadi Road"
    }
  )
}