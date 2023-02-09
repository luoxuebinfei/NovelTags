import serviceAxios from '../index'

export const getUserInfo = (params) => {
  return serviceAxios({
    url: '/api/website/queryMenuWebsite',
    method: 'post',
    params
  })
}
export const login = (data) => {
  return serviceAxios({
    url: '/api/user/login',
    method: 'post',
    data
  })
}

export const test = () => {
  return serviceAxios({
    url: '/',
    method: 'get'
  })
}
