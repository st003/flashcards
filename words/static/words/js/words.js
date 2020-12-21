function getNewWord() {
    fetch('/get_word/')
        .then(res => res.json())
        .then(data => {
            document.getElementById('en').innerHTML = data.en;
            document.getElementById('jp').innerHTML = data.jp;
        })
}


/* GLOBAL EVENT LISTENERS */
document.addEventListener('DOMContentLoaded', () => {
    
    if (document.getElementById('flashcard')) {
        
        // on initial page load
        getNewWord();

        document.getElementById('flipCardBtn').addEventListener('click', () => {
            // hide flip button and japanese
            document.getElementById('jp').style.display = 'none';
            document.getElementById('flipCardBtn').style.display = 'none';
            // reveal english text and next button
            document.getElementById('en').style.display = 'block';
            document.getElementById('newCardBtn').style.display = 'block';
        })

        document.getElementById('newCardBtn').addEventListener('click', () => {
            // hide english text and next button
            document.getElementById('newCardBtn').style.display = 'none';
            document.getElementById('en').style.display = 'none';
            // reveal flip card button and request a new word
            document.getElementById('flipCardBtn').style.display = 'block';
            document.getElementById('jp').style.display = 'block';
            getNewWord();
        })
    }
})
