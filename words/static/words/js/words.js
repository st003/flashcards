function getNewWord(last_id) {
    // set id to 0 if last_id is undefined
    const id = last_id ? last_id : 0;
    fetch(`/get_word/?id=${id}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById('id').innerHTML = data.id;
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
            document.getElementById('en').style.display = 'none';
            document.getElementById('flipCardBtn').style.display = 'none';
            // reveal english text and next button
            document.getElementById('jp').style.display = 'block';
            document.getElementById('newCardBtn').style.display = 'block';
        })

        document.getElementById('newCardBtn').addEventListener('click', () => {
            // hide english text and next button
            document.getElementById('newCardBtn').style.display = 'none';
            document.getElementById('jp').style.display = 'none';
            // reveal flip card button and request a new word
            document.getElementById('flipCardBtn').style.display = 'block';
            document.getElementById('en').style.display = 'block';
            getNewWord(document.getElementById('id').value);
        })
    }
})
