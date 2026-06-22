document.getElementById("reviewBtn").addEventListener("click", async () => {

    const code =
        document.getElementById("codeInput").value;

    const output =
        document.getElementById("output");

    output.innerText =
        "⏳ Reviewing code using AI...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/review",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    code: code
                })
            }
        );

        const data =
            await response.json();

        output.innerText =
            data.response;

    } catch (error) {

        output.innerText =
            "Error connecting to backend.";

        console.error(error);
    }

});

document.getElementById("downloadBtn").addEventListener("click", () => {

    const reviewText =
        document.getElementById("output").innerText;

    const blob = new Blob(
        [reviewText],
        {
            type: "text/plain"
        }
    );

    const link =
        document.createElement("a");

    link.href =
        URL.createObjectURL(blob);

    link.download =
        "review.txt";

    link.click();

});