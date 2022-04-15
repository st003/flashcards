var app = new Vue({
    // required change b/c django uses {{ }}
    // for its template rendering
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        count: 0,
        categories: [],
        category: 0,
        categorySelection: 0,
        topics: [],
        topic: 'All',
        topicSelection: 'All',
        en: '',
        jp: '',
        cardIsFlipped: false,
        showFilters: false,
        fadeOut: false,
        error: false,
        filterChange: false
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
    watch: {
        category: function() { this.filterChange = true },
        topic: function() { this.filterChange = true }
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
            let uri = '/get_word/?'
            if (this.category != 0) uri += `&category=${this.category}`
            if (this.topic != 'All') uri += `&topic=${this.topic}`
            if (this.filterChange) uri += `&purgeMem=true`

            fetch(uri)
                .then(res => {
                    if (res.status === 404) return Promise.reject(new Error('404'))
                    else return Promise.resolve(res.json())
                })
                .then(data => {
                    this.error = false
                    this.count = data.count
                    this.en = data.en
                    this.jp = data.jp
                    this.filterChange = false
                })
                .catch(() => {
                    this.count = 0
                    this.error = true
                })
        },
        openFilters() {
            this.fadeOut = false;
            this.showFilters = true;
        },
        closeFilters() {
            this.fadeOut = true;
            setTimeout(() => { this.showFilters = false; }, 350);
        },
        resetFilters() {
            this.categorySelection = 0;
            this.topicSelection = 'All';
        },
        applyFilters() {
            this.category = this.categorySelection;
            this.topic = this.topicSelection;
            this.cardIsFlipped = false;
            this.getNewWord();
            this.closeFilters();
        },
        flipCard() {
            this.cardIsFlipped = true;
        },
        nextCard() {
            this.getNewWord()
            this.cardIsFlipped = false;
        }
    }
})
