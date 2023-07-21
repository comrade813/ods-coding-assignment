import axios, { AxiosError, AxiosResponse } from 'axios';

async function request(url: string,
        onSuccess: (response: AxiosResponse<any,any>) => void,
        onFailure: (error: AxiosError) => void) {
    console.log(process.env.NODE_ENV)
    return await axios.get(process.env.REACT_APP_BACKEND_URL + url).then(
        (response) => { onSuccess(response) }
    ).catch((error) => { onFailure(error) });
}

export {
    request
}