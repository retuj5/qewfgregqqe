module.exports = {
    chainWebpack: config => {
        config
            .plugin('html')
            .tap(args => {
                args[0].title = '唐哼哼博客'
                return args
            })
    }
}