let startTime = Date.now(); /* 開始時間を保存する変数 */
let correct = 0;            /* 正解数を保存する変数 */
let count = 0;              /* 解いた問題数を保存する変数 */

let lastResult = "";        /* 前問の判定結果を保存する変数 */

let wrongProblems = [];     /* まちがえた問題を保存する配列 */
let currentProblem = null;  /* 現在の問題を保存する変数 */

function submitAnswer(){

    let userAnswer = "";

    if(currentProblem.answer_type == "int" ||
       currentProblem.answer_type == "dec"){

        userAnswer =
            document.getElementById("answer-input").value;
    }

    if(currentProblem.answer_type == "fra"){

        let num =
            document.getElementById("num").value;

        let den =
            document.getElementById("den").value;

        if(num == "" || den == ""){
            alert("ぶんしとぶんぼをいれてね！");
            return;
        }

        userAnswer = num + "/" + den;
    }

    if(currentProblem.answer_type == "rem"){

        let q =
            document.getElementById("q").value;

        let r =
            document.getElementById("r").value;

        if(r == ""){
            userAnswer = q;
        }else{
            userAnswer = q + "あまり" + r;
        }
    }

    count++;

    let isCorrect = false;

    if(userAnswer == currentProblem.answer){
        isCorrect = true;
    }

    if(isCorrect){
        lastResult = "せいかい！🎉";
        correct++;
    }else{
        lastResult = "おしい！";
        wrongProblems.push(currentProblem);
    }

    loadProblem();
}

async function loadProblem(){
    /* 前問の判定結果を表示 */
    document.getElementById("result").innerText = lastResult;
    
    /* 進捗バーを表示 */
    let percent = (count / MAX_PROBLEM) * 100;

    document.getElementById("progress-fill").style.width =
    percent + "%";

    /* 最後まで問題を解き終わった場合の処理 */
    if(count >= MAX_PROBLEM){
        /* 計測時間・正答率を計算 */
        let endTime = Date.now();
        let time = (endTime - startTime) / 1000;
        let rate = correct / MAX_PROBLEM * 100;

        /* まちがえた問題があればもう一回やる */        
        if(wrongProblems.length > 0){

            problems = wrongProblems;
            wrongProblems = [];
            count = 0;

            alert("まちがえた問題をもう一回やろう！");
            loadProblem();
            return;
        }

        /* 結果画面へ遷移 */
        window.location.href = 
            "/result?time=" + time + "&rate=" + rate;

        return;
    }

    document.getElementById("progress").innerText =
        (count + 1) + " / " + MAX_PROBLEM;


    /* APIから問題を取得 */
    const res = await fetch("/api/problem");
    const data = await res.json();


    /* 現在の問題を保存 */
    const problem = data.problem;

    currentProblem = problem;

    document.getElementById("question").innerText = problem.question;

    
    /* 難易度が2以上の場合は入力形式で回答させる */
    if(data.difficulty >= 2){

        document.getElementById("choices-area").style.display="none";
        document.getElementById("input-area").style.display="block";

        if(problem.answer_type == "int" || problem.answer_type == "dec"){
            document.getElementById("input-int-dec").style.display="block";
            document.getElementById("input-fraction").style.display="none";
            document.getElementById("input-remain").style.display="none";
        }

        if(problem.answer_type == "fra"){
            document.getElementById("input-int-dec").style.display="none";
            document.getElementById("input-fraction").style.display="block";
            document.getElementById("input-remain").style.display="none";
        }

        if(problem.answer_type == "rem"){
            document.getElementById("input-int-dec").style.display="none";
            document.getElementById("input-fraction").style.display="none";
            document.getElementById("input-remain").style.display="block";
        }

    }

    /* 難易度が1の場合のみ選択肢のボタンを表示 */
    if(data.difficulty == 1){
        document.getElementById("choices-area").style.display="block";
        document.getElementById("input-area").style.display="none";
    }else{
        document.getElementById("choices-area").style.display="none";
        document.getElementById("input-area").style.display="block";
    }

    /* 難易度が1の場合のみ４択のボタン押す */
    const buttons = document.querySelectorAll(".choice");

    buttons.forEach((btn, i) => {

        btn.innerText = problem.choices[i];

        btn.onclick = () => {

            count++;

            let isCorrect = false;

            if(problem.choices[i] == problem.answer){
                isCorrect = true;
            }

            if(isCorrect){
                lastResult = "せいかい！🎉";
                correct++;
            }else{
                lastResult = "おしい！";
                wrongProblems.push(problem);
            }

            loadProblem();
        }
    });

}

if (document.getElementById("question")) {
    loadProblem();
}

/* エンターキーで回答を提出できるようにする */
document.addEventListener("keydown", function(e){
    if(e.key === "Enter"){
        submitAnswer();
    }
});