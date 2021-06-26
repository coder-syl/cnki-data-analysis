// vue.config.js
const path = require('path');

module.exports = {
    lintOnSave: false,
    devServer: {
        proxy: {
            '/cnki': {
                target: 'http://localhost:8000/',
                changeOrigin: true,   // 允许跨域
            }
        }
    },
    configureWebpack: {
        resolve: {
            alias: {
                '@': path.resolve(__dirname, './src'),

            },
        },
    },
}