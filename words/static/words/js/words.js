var app = new Vue({
    // required change b/c django uses {{ }}
    // for its template rendering
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        count: 0,
        categories: [],
        category: 0,
        topics: [],
        topic: 'All',
        en: '',
        jp: '',
        cardIsFlipped: false,
        showFilters: false,
        error: false,
    },
    computed: {
        currentCategory() {
            let categoryName = 'All'
            if (this.category != 0) {
                this.categories.forEach(c => {
                    if (c.value == this.category) {
                        categoryName = c.name
                    }
                })
            }
            return categoryName
        }
    },
    created: function () {
        fetch('/get_category/')
            .then(res => res.json())
            .then(data => { this.categories = data.categories })
        fetch('/get_topic/')
            .then(res => res.json())
            .then(data => { this.topics = data.topics })
        this.getNewWord() 
    },
    methods: {
        getNewWord() {
            // dynamic query string builder. I hate this.
            // fetch is garbage
            let query = '/get_word/?'
            if (this.category != 0) query += `&category=${this.category}`
            if (this.topic != 'All') query += `&topic=${this.topic}`

            fetch(query)
                .then(res => {
                    if (res.status === 404) return Promise.reject(new Error('404'))
                    else return Promise.resolve(res.json())
                })
                .then(data => {
                    this.error = false
                    this.count = data.count
                    this.en = data.en
                    this.jp = data.jp
                })
                .catch(() => {
                    this.count = 0
                    this.error = true
                })
        },
        openFilters() {
            this.showFilters = true
        },
        closeFilters() {
            this.showFilters = false
        },
        resetFilters() {
            this.category = 0
            this.topic = 'All'
        },
        applyFilters() {
            this.cardIsFlipped = false
            this.getNewWord()
            this.closeFilters()
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
