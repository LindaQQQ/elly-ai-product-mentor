# AI Product Mentor Demo Flow

## Demo Goal

Show that AI Product Mentor is not another PRD generator. It helps PMs improve
the quality of product decisions—from challenging an idea to planning an AI
solution and identifying how it should be validated.

Recommended duration: **4–5 minutes**.

## Demo Story

Use one consistent scenario throughout the demo:

> A SaaS company wants to build an AI customer-support assistant that answers
> common questions and transfers the conversation to a human when it cannot
> provide a reliable answer.

## Before the Demo

1. Start the FastAPI service from `backend`.
2. Open `http://127.0.0.1:8000/app`.
3. Confirm AI Planning is selected.
4. Keep the form empty at the beginning.
5. If the live Mentor API is not configured, describe Challenge Idea and Product
   Decision briefly without submitting a chat message.

## 1. Opening — The Problem (30 seconds)

### Say

> 很多 PM 已經知道想做 AI，但不知道這個需求是否真的適合 AI、應該用
> Workflow、RAG 還是 Agent，也不知道最重要的風險與下一步問題。
>
> AI Product Mentor 不只是幫 PM 寫文件，而是像 Senior PM 一樣，先幫你
> 挑戰想法、做決策，再把 AI 產品規劃清楚。

### Show

Point to the left navigation:

- Challenge Idea
- Product Decision
- AI Planning
- AI Spec — Coming Soon
- AI Evaluation — Coming Soon

### Key Message

The product supports a continuous journey, not a collection of unrelated AI
writing tools.

## 2. Existing Foundation — Challenge and Decision (30–45 seconds)

### Show

Select **Challenge Idea**, then **Product Decision**.

### Say

> Challenge Idea 會先挑戰需求背後的假設；Product Decision 則幫 PM 比較
> 選項、限制與取捨。這兩個既有能力回答的是：「我們該不該做、先做什麼？」
>
> 但當答案是「我們要做一個 AI Feature」，PM 接下來還有另一組問題。

Return to **AI Planning**.

## 3. Enter a Real AI Requirement (45 seconds)

Fill the form with the following values.

### Requirement Description

```text
打造一個客服 AI，回答常見問題；無法確認答案時自動轉接真人。
```

### Product Goal

```text
降低客服首次回覆時間 50%
```

### Primary User

```text
使用 SaaS 後台的中小企業客戶
```

### Acceptable Error Risk

Select:

```text
中 — 可由人工補救或確認
```

### Knowledge Source

Select:

```text
FAQ／Help Center
```

### Say

> Mentor 不要求 PM 先寫完整 PRD。它只先收集會真正影響 AI 方案的資訊：
> 問題、目標、使用者、錯誤風險與知識來源。

## 4. Analyze (10 seconds)

Select **Analyze with AI Mentor**.

### Say

> 這一版先用前端 mock data 驗證規劃流程與結果是否有用，還沒有把 AI
> Planning 接到正式後端 Agent。

Do not hide this prototype boundary. It builds trust and keeps the demo focused
on the product hypothesis being tested.

## 5. Explain the Result (90 seconds)

### AI Readiness

Point to the score and suitability result.

### Say

> Mentor 不會只說「可以用 AI」。它會拆解問題清楚度、資料準備度與風險
> 是否可控。這個案例有重複性任務，也有 FAQ 知識來源，所以初步適合 AI；
> 但需要可靠的 fallback。

### Recommended Solution

Point to **Workflow**, **RAG**, and **Tools**. Contrast them with the unselected
**Agent** and **Memory**.

### Say

> Mentor 建議先用 Workflow 加 RAG，不急著做自主 Agent。使用者問題先做
> 意圖判斷，再檢索 FAQ；回答要附來源，信心不足就用 Tool 建立轉接工單。
>
> Memory 暫時不是必要能力，因為這個 MVP 的核心是正確回答既有知識，
> 不是建立長期個人化關係。

### Key Message

AI Product Mentor recommends the smallest controllable architecture—not the most
complex or fashionable architecture.

## 6. Risks and Next Questions (45 seconds)

### Say

> 真正有價值的不只是架構圖，而是讓 PM 在開發前看到容易忽略的風險：
> 回答錯誤、知識過期、權限與個資。
>
> 接著 Mentor 把模糊需求轉成三個可以行動的問題：哪些情境一定要真人、
> FAQ 誰負責更新，以及成功除了速度之外要怎麼衡量品質。

Point to **Main Risks** and **Next Questions** while speaking.

## 7. Closing — Product Direction (30 seconds)

### Say

> 這就是 AI Product Mentor 的完整方向：從 Challenge Idea、Product Decision，
> 走到 AI Planning；下一步會把規劃結果轉成 AI Spec，再建立 Evaluation
> Dataset、Rubric 與上線驗收方式。
>
> 我們不是幫 PM 更快產生文件，而是陪 PM 做出更好的 AI 產品決策。

## Suggested Closing Slide or Sentence

> **From product idea to an AI solution you can explain, control, and evaluate.**

## Backup Plan

If the Mentor chat API fails during the demo:

1. Do not troubleshoot it live.
2. Explain Challenge Idea and Product Decision through the navigation only.
3. Return to AI Planning.
4. Complete the frontend analysis, which does not depend on the backend model.

## Demo Checklist

- [ ] Local service is running
- [ ] AI Planning page loads
- [ ] Form fields accept input
- [ ] Analyze displays the mock result
- [ ] Challenge Idea and Product Decision navigation works
- [ ] The presenter states that Planning currently uses mock data
- [ ] The demo ends with AI Spec and AI Evaluation as the next product stages
