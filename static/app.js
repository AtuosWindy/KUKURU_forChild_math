let lastResult = "";        /* 前問の判定結果を保存する変数 */
let currentProblem = null;  /* 現在の問題を保存する変数 */
let maxNum = 0;             /* 出題される数の最大値を保存する変数 */
let userAnswer = "";


async function submitAnswer(){

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

    const res = await fetch("/api/answer", {
        method: "POST",

        headers: {"Content-Type": "application/json"},

        body: JSON.stringify({answer: userAnswer}),
    });

    const data = await res.json();

    if(data.is_correct){
        lastResult = "せいかい！🎉";
    }else{ 
        lastResult = "おしい！";
    }

    loadProblem();
    return;
}

async function loadProblem(){
    /* APIから問題を取得 */
    const res = await fetch("/api/problem");
    const data = await res.json();
    

    if(data.status == "finished"){
        /* 結果画面へ遷移 */
        window.location.href = "/result";
        return;
    }
    else if(data.status == "retry_prompt"){
        if(confirm("まちがえた問題をもう一回やる？")){
            await fetch("/api/retry", {method: "POST"});
            loadProblem();
        } else {
            window.location.href = "/result";
        }
        return;
    }


    /* 入力欄を空にする */
    document.getElementById("answer-input").value = "";

    document.getElementById("num").value = "";
    document.getElementById("den").value = "";

    document.getElementById("q").value = "";
    document.getElementById("r").value = "";


    /* 今何番目の問題か */
    let count = data.index + 1;
    
    if(count - 1 > 0){
        /* 前問の判定結果を表示 */
        document.getElementById("result").innerText = lastResult;
    }



    /* 出題される数の最大値を保存 */
    maxNum = data.max_index;
    /* まちがえた問題をもう一回やる場合は、出題される数の最大値をまちがえた問題数にする */
    /* ただしそれは /api/problem にて仕分け済みであるため、特に何もしなくていい */

    /* 進捗バーを表示 */
    let percent = (count / maxNum) * 100;

    document.getElementById("progress-fill").style.width =
    percent + "%";

    /* 今何問目かを表示 */
    document.getElementById("progress").innerText =
        (count) + " / " + maxNum;




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
    else if(data.difficulty == 1){
        document.getElementById("choices-area").style.display="block";
        document.getElementById("input-area").style.display="none";
    }

    /* 難易度が1の場合のみ４択のボタン押す */
    const buttons = document.querySelectorAll(".choice");

    buttons.forEach((btn, i) => {

        btn.innerText = problem.choices[i];

        btn.onclick = async () => {

            userAnswer = problem.choices[i];
            /* console.log("送る値:", userAnswer); */

            const res = await fetch("/api/answer", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({answer: String(userAnswer)}),
            });
            const data = await res.json();

            if(data.is_correct){
                lastResult = "せいかい！🎉";
            }else{ 
                lastResult = "おしい！";
            }

            loadProblem();
            return;
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

