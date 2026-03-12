let count = 0;
const MAX_PROBLEM = 10;
let startTime = Date.now();
let correct = 0;
let lastResult = "";

async function startGame(){

    await fetch("/start");

    location.href = "/problem";
}

async function loadProblem(){

    document.getElementById("result").innerText = lastResult;

    if(count >= MAX_PROBLEM){

        let endTime = Date.now();
        let time = (endTime - startTime) / 1000;
        let rate = correct / MAX_PROBLEM * 100;

        window.location.href = 
            "/result?time=" + time + "&rate=" + rate;

        return;
    }

    document.getElementById("progress").innerText =
        (count + 1) + " / " + MAX_PROBLEM;

    const res = await fetch("/api/problem");
    const data = await res.json();

    document.getElementById("question").innerText = data.question;

    const buttons = document.querySelectorAll(".choice");

    buttons.forEach((btn, i) => {

        btn.innerText = data.choices[i];

        btn.onclick = () => {

            count++;

            if(data.choices[i] == data.answer){
                lastResult = "せいかい！🎉";
                correct++;
            }else{
                lastResult = "ちがうよ！";
            }

            loadProblem();
        }
    });
}

if (document.getElementById("question")) {
    loadProblem();
}