import axios from 'axios'
import {Message} from 'element-ui'
import nprogress from 'nprogress'
import 'nprogress/nprogress.css'

// create an axios instance
const service = axios.create({
    headers: {
        'Access-Control-Allow-Origin': '*',
    },
    crossDomain: true,
    contentType: "application/json",
    baseURL: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:2020/api' : '', // api的base_url
    timeout: 5000 // request timeout
})
service.interceptors.request.use(config => {
    nprogress.start()
    console.log(process.env.NODE_ENV)
    return config
}, error => {
    console.log(error) // for debug
    Promise.reject(error).then(r => {
        console.log(r)
    })
})

service.interceptors.response.use(
    response => {
        nprogress.done()
        checkStatus(response)
        return response
    },
    error => {
        nprogress.done()
        checkStatus(error.response)
        // 统一扶正错误状态 30X,40X,50X等异常，后续不需要再写catch
        return Promise.resolve(error.response)
    })

/**
 * 统一判断返回状态值
 * response {
 *  status,  // http 响应状态
 *  data {   //服务器返回内容封装
 *      code: 服务器业务码
 *      msg:  提示消息
 *      resultList: 结果列表
 *      resultObject: 结果对象
 *      pages: 页数
 *      total: 总数
 *      debug: 调试信息
 *    }
 * }
 */
function checkStatus(response) {
    if (response === undefined) {
        Message({
            message: '服务器请求超时',
            type: 'error',
            dangerouslyUseHTMLString: true,
            duration: 5 * 1000
        })
        Promise.reject('请求超时').then(r => {
            console.log(r)
        })
        return
    }

    if (response.status === 200) {
        if (response.data !== undefined && response.data.code !== undefined && response.data.code !== 200) {
            let errorMessage = response.data.msg + '<br/><br/>' + '错误码: ' + response.data.code;
            if (response.data.debug) {
                errorMessage += '服务端调试信息:' + JSON.stringify(response.data.debug)
            }
            Message({
                message: errorMessage,
                showClose: true,
                type: 'error',
                dangerouslyUseHTMLString: true,
                duration: 5 * 1000
            })
            // 重新登陆
            if (response.data.code === 10003) {
                // store.dispatch('FedLogOut').then(() => {
                //     location.reload()
                // })
            }
        }
        return response
    }

    // 服务器请求异常
    if (response.status === 500 || response.status === 422) {
        const errorMessage = response.data.msg + '<br/><br/>' + '错误码: ' + response.data.code
        if (response.data.debug) {
            console.error('服务端调试信息:' + JSON.stringify(response.data.debug))
        }
        Message({
            message: errorMessage,
            showClose: true,
            type: 'error',
            dangerouslyUseHTMLString: true,
            duration: 5 * 1000
        })
        return response
    }
    if (response.status === 401) {
        Message({
            message: '登录已过期',
            showClose: true,
            type: 'error',
            center: true,
            duration: 5 * 1000
        })
        // store.dispatch('FedLogOut').then(() => {
        //     location.reload()
        // })
        return response
    }
    if (response.status === 404) {
        Message({
            message: '无效请求',
            showClose: true,
            type: 'error',
            center: true,
            duration: 5 * 1000
        })
        return response
    }
    if (response.status === 403) {
        Message({
            message: '无权访问' + response.data,
            showClose: true,
            type: 'error',
            center: true,
            duration: 5 * 1000
        })
        return response
    }
    return response
}

export default service
