<template>
    <div class="container__formBlock">
        <div class="containerForm">
            <div style="display: block;">
                <h1>ОСТАЛИСЬ ВОПРОСЫ?</h1>
                <p>Заполните форму, и наш администратор в скором времени свяжется с вами, чтобы ответить на все вопросы</p>
                <input type="text" placeholder="Ваше имя">
                <input type="text" placeholder="yourmail@example.com">
                <input type="tel" placeholder="+ 7 (900) 900-90-90">
                <button>Оставить заявку</button>
            </div>
            <div>
                <img class="img2In__firmBlock" src="/public/bgStart.png" style="width: 90%; border-radius: 20px; height: 100%; margin-left: 10%;">
            </div>
        </div>
    </div>
</template>

<style>
.container__formBlock {
    background-image: url("/public/bgStart.png");

    padding: 10vh;

    height: 100vh;
}

.containerForm {
    border: 2px solid var(--vt-text2-color);
    border-radius: 20px;

    display: flex;
    padding: 40px;

    color: var(--vt-text2-color);

    background: rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);

    div{
        h1 {
            margin-top: 0;
        }
        input {
            margin-top: 30px;
            width: 300px;
        }
        button {
            font-size: 26px;

            margin-top: 30px;

            padding: 5px 50px;
            width: 100%;

            box-shadow: none;
            border: none;
        }

        button:hover {
            border: none;
        }
    }
}

@media(max-width: 1024px) {
    .img2In__firmBlock {
        display: none;
    }
    .containerForm {
        text-align: center;
        padding: 20px;
        div {
            input {
                width: 80%;
            }
            button {
                font-size: 4vw;
            }
        }
    }
    .container__formBlock {
        padding: 20% 5%;
    }
}
</style>