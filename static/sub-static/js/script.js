(function ($) {

    // scroll functions
    $(window).scroll(function(e) {
    
        // add/remove class to navbar when scrolling to hide/show
        var scroll = $(window).scrollTop();
        if (scroll >= 150) {
            $('.navbar').addClass("navbar-hide");
        } else {
             $('.navbar').removeClass("navbar-hide");
        }
    
    });
    
})(jQuery);  


// select box of town with cheack box

var expanded = false;

function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}


// change case of case-donate

function change(){

    var listDonate = document.getElementById("donate-kind"),
        
        list = document.getElementById("list"),

        button = document.getElementById('donate'),

        sub_menu = document.getElementById('sub_menu')


    if(listDonate.value == "general"){

       list.setAttribute('disabled' , true)
       sub_menu.setAttribute('disabled' , true)
    }
 
    else{
        
        list.removeAttribute('disabled')
    }

    if(listDonate.value == "case"){

        button.value = "إظهر النتائج"
    }

    else {

        button.textContent = "تبرع"
    }

   
}


//change case of Baramg

function changed(){

    var social = document.getElementById("social"),

        development = document.getElementById("development"),

        medical = document.getElementById("medical"),

        economic = document.getElementById("economic")

        list = document.getElementById("list");

        sub_menu = document.getElementById('sub_menu')

    document.getElementById("sub_menu").value= "";

 

    if(list.value=='one'){
        sub_menu.removeAttribute('disabled')

        social.style.display ='block'
        development.style.display = 'none' 
        medical.style.display = 'none'
        economic.style.display = 'none'     
    }
        
    else if(list.value=='two'){
        sub_menu.removeAttribute('disabled')
        social.style.display='none'
        economic.style.display = 'none' 
        economic.style.display = 'none' 
        development.style.display = 'block'    
    }

    else if(list.value=='three'){
        sub_menu.removeAttribute('disabled')
        social.style.display='none'
        development.style.display = 'none' 
        economic.style.display = 'none' 
        medical.style.display = 'block' 
    }

    else{
        sub_menu.removeAttribute('disabled')
        social.style.display='none'
        development.style.display = 'none' 
        medical.style.display = 'none'
        economic.style.display = 'block' 
    }
    
}

/* amount of money and trade zakat  */

function calc(){

    var howMuch = parseInt(document.getElementById("howMuch").value) ;

    document.getElementById("amount").value= howMuch * .025; 

    document.getElementById("donat").value = howMuch * .025;

    if(isNaN(howMuch)){
        document.getElementById("amount").value="" 
        document.getElementById("donat").value = ""
    } 
    
}

 /*gold zakat and silver zakat */

function calcu(){
    var muchGold =parseInt(document.getElementById("muchGold").value) ,

        amGold =parseInt(document.getElementById("amGold").value)  ,

        amZakat = muchGold * amGold * .025 ;

        document.getElementById("amZakat").value= amZakat;

        document.getElementById("aGold").value = amZakat;

        if(isNaN(muchGold)){
            document.getElementById("amZakat").value="" 
            document.getElementById("aGold").value = ""
        } 
}

/* land zakat */

function cal(){
    var howMuch = parseInt(document.getElementById("howMuch").value) ;

    document.getElementById("amount").value= howMuch * .25; 

    document.getElementById("donat").value = howMuch * .25;

    if(isNaN(howMuch)){
        document.getElementById("amount").value="" 
        document.getElementById("donat").value = ""
    } 
}

/* out of land zakat */

function calu(){
    var howMuch = parseInt(document.getElementById("howMuch").value) ;

    document.getElementById("amount").value= howMuch * .05; 

    document.getElementById("donat").value = howMuch * .05;

    if(isNaN(howMuch)){
        document.getElementById("amount").value="" 
        document.getElementById("donat").value = ""
    } 
}

/* fetr zakat */

function caluc(){
    var howMuch = parseInt(document.getElementById("howMuch").value) ;

    document.getElementById("amount").value= howMuch * 15; 

    document.getElementById("donat").value = howMuch * 15;

    if(isNaN(howMuch)){
        document.getElementById("amount").value="" 
        document.getElementById("donat").value = ""
    } 
}

/* rekaz zakat */

function calucu(){
    var howMuch = parseInt(document.getElementById("howMuch").value) ;

    document.getElementById("amount").value= howMuch * .2; 

    document.getElementById("donat").value = howMuch * .2;

    if(isNaN(howMuch)){
        document.getElementById("amount").value="" 
        document.getElementById("donat").value = ""
    } 
}

/* FAQ */

var answer_one = document.getElementById("answer_one") ,

    answer_two = document.getElementById("answer_two") ,

    answer_three = document.getElementById("answer_three") ,

    answer_four = document.getElementById("answer_four") ,

    answer_five = document.getElementById("answer_five") ,

    answer_six = document.getElementById("answer_six") ,

    answer_seven = document.getElementById("answer_seven") ;


function ques_one(){
    answer_one.style.display = 'block'
    answer_two.style.display = 'none'
    answer_three.style.display = 'none'
    answer_four.style.display = 'none'
    answer_five.style.display = 'none'
    answer_six.style.display = 'none'
    answer_seven.style.display = 'none'

    document.getElementById("i1").classList.add("active")
    document.getElementById("label1").classList.add("active")
    document.getElementById("i2").classList.remove("active")
    document.getElementById("label2").classList.remove("active")
    document.getElementById("i3").classList.remove("active")
    document.getElementById("label3").classList.remove("active")
    document.getElementById("i4").classList.remove("active")
    document.getElementById("label4").classList.remove("active")
    document.getElementById("i5").classList.remove("active")
    document.getElementById("label5").classList.remove("active")
    document.getElementById("i6").classList.remove("active")
    document.getElementById("label6").classList.remove("active")
    document.getElementById("i7").classList.remove("active")
    document.getElementById("label7").classList.remove("active")

}

function ques_two(){
    answer_one.style.display = 'none'
    answer_two.style.display = 'block'
    answer_three.style.display = 'none'
    answer_four.style.display = 'none'
    answer_five.style.display = 'none'
    answer_six.style.display = 'none'
    answer_seven.style.display = 'none'

    document.getElementById("i1").classList.remove("active")
    document.getElementById("label1").classList.remove("active")
    document.getElementById("i2").classList.add("active")
    document.getElementById("label2").classList.add("active")
    document.getElementById("i3").classList.remove("active")
    document.getElementById("label3").classList.remove("active")
    document.getElementById("i4").classList.remove("active")
    document.getElementById("label4").classList.remove("active")
    document.getElementById("i5").classList.remove("active")
    document.getElementById("label5").classList.remove("active")
    document.getElementById("i6").classList.remove("active")
    document.getElementById("label6").classList.remove("active")
    document.getElementById("i7").classList.remove("active")
    document.getElementById("label7").classList.remove("active")
}

function ques_three(){
    answer_one.style.display = 'none'
    answer_two.style.display = 'none'
    answer_three.style.display = 'block'
    answer_four.style.display = 'none'
    answer_five.style.display = 'none'
    answer_six.style.display = 'none'
    answer_seven.style.display = 'none'

    document.getElementById("i1").classList.remove("active")
    document.getElementById("label1").classList.remove("active")
    document.getElementById("i2").classList.remove("active")
    document.getElementById("label2").classList.remove("active")
    document.getElementById("i3").classList.add("active")
    document.getElementById("label3").classList.add("active")
    document.getElementById("i4").classList.remove("active")
    document.getElementById("label4").classList.remove("active")
    document.getElementById("i5").classList.remove("active")
    document.getElementById("label5").classList.remove("active")
    document.getElementById("i6").classList.remove("active")
    document.getElementById("label6").classList.remove("active")
    document.getElementById("i7").classList.remove("active")
    document.getElementById("label7").classList.remove("active")
}

function ques_four(){
    answer_one.style.display = 'none'
    answer_two.style.display = 'none'
    answer_three.style.display = 'none'
    answer_four.style.display = 'block'
    answer_five.style.display = 'none'
    answer_six.style.display = 'none'
    answer_seven.style.display = 'none'

    document.getElementById("i1").classList.remove("active")
    document.getElementById("label1").classList.remove("active")
    document.getElementById("i2").classList.remove("active")
    document.getElementById("label2").classList.remove("active")
    document.getElementById("i3").classList.remove("active")
    document.getElementById("label3").classList.remove("active")
    document.getElementById("i4").classList.add("active")
    document.getElementById("label4").classList.add("active")
    document.getElementById("i5").classList.remove("active")
    document.getElementById("label5").classList.remove("active")
    document.getElementById("i6").classList.remove("active")
    document.getElementById("label6").classList.remove("active")
    document.getElementById("i7").classList.remove("active")
    document.getElementById("label7").classList.remove("active")
}

function ques_five(){
    answer_one.style.display = 'none'
    answer_two.style.display = 'none'
    answer_three.style.display = 'none'
    answer_four.style.display = 'none'
    answer_five.style.display = 'block'
    answer_six.style.display = 'none'
    answer_seven.style.display = 'none'

    document.getElementById("i1").classList.remove("active")
    document.getElementById("label1").classList.remove("active")
    document.getElementById("i2").classList.remove("active")
    document.getElementById("label2").classList.remove("active")
    document.getElementById("i3").classList.remove("active")
    document.getElementById("label3").classList.remove("active")
    document.getElementById("i4").classList.remove("active")
    document.getElementById("label4").classList.remove("active")
    document.getElementById("i5").classList.add("active")
    document.getElementById("label5").classList.add("active")
    document.getElementById("i6").classList.remove("active")
    document.getElementById("label6").classList.remove("active")
    document.getElementById("i7").classList.remove("active")
    document.getElementById("label7").classList.remove("active")
}

function ques_six(){
    answer_one.style.display = 'none'
    answer_two.style.display = 'none'
    answer_three.style.display = 'none'
    answer_four.style.display = 'none'
    answer_five.style.display = 'none'
    answer_six.style.display = 'block'
    answer_seven.style.display = 'none'

    document.getElementById("i1").classList.remove("active")
    document.getElementById("label1").classList.remove("active")
    document.getElementById("i2").classList.remove("active")
    document.getElementById("label2").classList.remove("active")
    document.getElementById("i3").classList.remove("active")
    document.getElementById("label3").classList.remove("active")
    document.getElementById("i4").classList.remove("active")
    document.getElementById("label4").classList.remove("active")
    document.getElementById("i5").classList.remove("active")
    document.getElementById("label5").classList.remove("active")
    document.getElementById("i6").classList.add("active")
    document.getElementById("label6").classList.add("active")
    document.getElementById("i7").classList.remove("active")
    document.getElementById("label7").classList.remove("active")
}

function ques_seven(){
    answer_one.style.display = 'none'
    answer_two.style.display = 'none'
    answer_three.style.display = 'none'
    answer_four.style.display = 'none'
    answer_five.style.display = 'none'
    answer_six.style.display = 'none'
    answer_seven.style.display = 'block'

    document.getElementById("i1").classList.remove("active")
    document.getElementById("label1").classList.remove("active")
    document.getElementById("i2").classList.remove("active")
    document.getElementById("label2").classList.remove("active")
    document.getElementById("i3").classList.remove("active")
    document.getElementById("label3").classList.remove("active")
    document.getElementById("i4").classList.remove("active")
    document.getElementById("label4").classList.remove("active")
    document.getElementById("i5").classList.remove("active")
    document.getElementById("label5").classList.remove("active")
    document.getElementById("i6").classList.remove("active")
    document.getElementById("label6").classList.remove("active")
    document.getElementById("i7").classList.add("active")
    document.getElementById("label7").classList.add("active")
}


  


