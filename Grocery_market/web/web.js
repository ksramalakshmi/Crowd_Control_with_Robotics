document.querySelector("#addButton").onclick = function () { 

    var list = document.getElementById('list')
    var click = document.getElementById('addButton')
    var list_item = document.createElement("li")
    var item_name = document.getElementById('select').value
    var textNode = document.createTextNode(item_name);
    list_item.append(textNode)
    list.appendChild(list_item)

    eel.send_python(item_name)                   
    
  }

  document.querySelector("#clearbutton").onclick = function () { 

    var list = document.getElementById('list')
    list.removeChild(list.lastChild)
    
    eel.clear_python()
    
  }

document.querySelector("#donebutton").onclick = function(){
    eel.check_pos()(function(sum){
        var total = document.createElement('h1');
        total.innerHTML = "Net Total = Rs. "+sum;
        document.body.appendChild(total)
      }
    )
}