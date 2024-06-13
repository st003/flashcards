const { createApp } = Vue

createApp({
    // required change b/c django uses {{ }} for its template rendering
    delimiters: ['[[', ']]'],
    data() {
        return {
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
        }
    },
    computed: {
        currentCategory() {
            let categoryName = 'All'
            if (this.category != 0) {
                this.categories.forEach(c => {
                    if (c.value == this.category) {
                        categoryName = c.name;
                    }
                })
            }
            return categoryName;
        }
    },
    created: function () {
        fetch('/api/v1/category/')
            .then(res => res.json())
            .then(data => { this.categories = data });

        fetch('/api/v1/topic/')
            .then(res => res.json())
            .then(data => { this.topics = data });

        this.getCard()
            .then(data => this.setCard(data))
            .catch(() => this.setError());
    },
    methods: {
        setCard(data) {
            this.error = false;
            this.count = data.count;
            this.en = data.en;
            this.jp = data.jp;
            this.filterChange = false;
        },
        setError() {
            this.count = 0;
            this.error = true;
        },
        getCard() {
            const args = new URLSearchParams();
            if (this.category != 0) args.append('category', this.category);
            if (this.topic != 'All') args.append('topic', this.topic);
            if (this.filterChange) args.append('purgeMem', 'true');

            return new Promise((resolve, reject) => {
                fetch('/api/v1/word/rand/?' + args)
                    .then(res => {
                        if (res.status === 404) return Promise.reject(new Error('404'));
                        else return Promise.resolve(res.json());
                    })
                    .then(data => resolve(data))
                    .catch(() => reject());
            });
        },
        openFilters() {
            this.fadeOut = false;
            this.showFilters = true;
        },
        closeFilters() {
            this.fadeOut = true;
            setTimeout(() => { this.showFilters = false; }, 250);
        },
        resetFilters() {
            this.categorySelection = 0;
            this.topicSelection = 'All';
        },
        applyFilters() {

            this.category = this.categorySelection;
            this.topic = this.topicSelection;
            this.filterChange = true;

            this.getCard()
                .then(data => this.setCard(data))
                .catch(() => this.setError())
                .finally(() => {
                    this.closeFilters();
                    this.cardIsFlipped = false;
                });
        },
        flipCard() {
            this.cardIsFlipped = true;
        },
        nextCard() {
            this.getCard()
                .then(data => this.setCard(data))
                .catch(() => this.setError())
                .finally(() => { this.cardIsFlipped = false });
        }
    }
}).mount('#app');
