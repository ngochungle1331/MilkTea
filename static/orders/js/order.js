function select(id ,value){
    const mySelect = document.getElementById(id);
    // alert(mySelect)
        for (let j = 0; j < mySelect.options.length; j++) {
            if (mySelect.options[j].value == value) {
                // alert(mySelect[i].options[j].value + value)
                mySelect.options[j].selected = true;
              break;
            }        
    }
    
}


