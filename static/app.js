    let startTime = Date.now(); /* 開始時間を保存する変数 */
    let endTime = 0;            /* 終了時間を保存する変数 */
    let time;                   /* 経過時間を保存する変数 */

    let count = 0;              /* 解いた問題数を保存する変数 */
    let correct = 0;            /* 正解数を保存する変数 */
    let rate = 0;               /* 正答率を保存する変数 */

    let lastResult = "";        /* 前問の判定結果を保存する変数 */

    let wrongProblems = [];     /* まちがえた問題を保存する配列 */
    let wrongCount = 0;         /* まちがえた問題数を保存する変数 */
    let currentProblem = null;  /* 現在の問題を保存する変数 */

    let maxNum = 0;             /* 出題される数の最大値を保存する変数 */

    let problems = [];          /* API(または間違えた問題リスト)から取得した問題を保存する配列 */
    let problemIndex = 0;       /* 出題する問題のインデックスを保存する変数 */

    let retry_flag = false;     /* もう一度やるかどうかのフラグ */

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
        /* 入力欄を空にする */
        document.getElementById("answer-input").value = "";

        document.getElementById("num").value = "";
        document.getElementById("den").value = "";

        document.getElementById("q").value = "";
        document.getElementById("r").value = "";

        /* 前問の判定結果を表示 */
        if(!(retry_flag & count == 0)){
            document.getElementById("result").innerText = lastResult;
        }



        /* まちがえた問題をもう一回やる場合は、出題される数の最大値をまちがえた問題数にする */
        maxNum = (!retry_flag) ? MAX_PROBLEM : wrongCount;

        /* 進捗バーを表示 */
        let percent = (count / maxNum) * 100;

        document.getElementById("progress-fill").style.width =
        percent + "%";



        /* 最後まで問題を解き終わった場合の処理 */
        if(count >= maxNum){
            /* 計測時間・正答率を計算 */
            if(!retry_flag){
                endTime = Date.now();
                time = (endTime - startTime) / 1000;
                rate = correct / MAX_PROBLEM * 100;
            }

            /* まちがえた問題があればもう一回やる */        
            if(wrongProblems.length > 0){

                retry_flag = true;

                count = 0;
                wrongCount = wrongProblems.length;
                problems = wrongProblems;
                wrongProblems = [];

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
            (count + 1) + " / " + maxNum;


        /* APIから問題を取得 */
        const res = await fetch("/api/problem");
        const data = await res.json();


        /* 現在の問題を保存 */
        const problem = (!retry_flag) ? data.problem : problems[count];

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
                    correct += (!retry_flag) ? 1 : 0;
                }else{
                    lastResult = "おしい！";
                    wrongProblems.push(currentProblem);
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

    const res = await fetch("/api/answer", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answer: userAnswer})
    });

    /*
    const res = await fetch("/api/answer", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answer: userAnswer})
    })
    */

    const data = await res.json();

    if(data.is_correct){
        lastResult = "せいかい！🎉";
    }else{
        lastResult = "おしい！";
    }