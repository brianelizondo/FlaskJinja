const form = document.querySelector("form");

form.addEventListener("submit", function(event){
  event.preventDefault();
  
  const questions = document.querySelectorAll("form input");
  let question_answered = true;
  for(let question of questions){
    let answer = question.value;
    if(answer == "" || answer != answer.toLowerCase() || answer.length < 3){
      question_answered = false;
    }
  }
  if(!question_answered){
    alert("All questions must be answered, must be at least 3 characters long and must be in lowercase");
  }else{
    form.submit();
  }
})