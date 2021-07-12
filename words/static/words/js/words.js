var app = new Vue({
    // required change b/c django uses {{ }}
    // for its template rendering
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        count: 0,
        en: '',
        jp: '',
        cardIsFlipped: false,
        showFilters: false
    },
    created: function () {
        this.getNewWord()
    },
    methods: {
        getNewWord() {
            fetch('/get_word/')
                .then(res => res.json())
                .then(data => {
                    this.count = data.count
                    this.en = data.en
                    this.jp = data.jp
                })
        },
        openFilters() {
            this.showFilters = true
        },
        closeFilters() {
            this.showFilters = false
        },
        flipCard() {
            this.cardIsFlipped = true
        },
        nextCard() {
            this.getNewWord()
            this.cardIsFlipped = false
        }
    }
})
