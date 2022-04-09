const cepEl = document.getElementById('id_cep')
const logradouroEl = document.getElementById('id_logradouro')
const complementoEl = document.getElementById('id_complemento')
const bairroEl = document.getElementById('id_bairro')
const cidadeEl = document.getElementById('id_cidade')
const ufEl = document.getElementById('id_uf')

const consultarCep = () => {
    const cep = cepEl.value

    // {
    //     "cep": "01001-000",
    //     "logradouro": "Praça da Sé",
    //     "complemento": "lado ímpar",
    //     "bairro": "Sé",
    //     "localidade": "São Paulo",
    //     "uf": "SP",
    //     "ibge": "3550308",
    //     "gia": "1004",
    //     "ddd": "11",
    //     "siafi": "7107"
    //   }
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then(res => res.json())
    .then(end => {
        logradouroEl.value = end.logradouro
        complementoEl.value = end.complemento
        bairroEl.value = end.bairro
        cidadeEl.value = end.localidade
        ufEl.value = end.uf
    })
    .catch(() => alert("Não foi possível consultar seu cep"))
}

cepEl.addEventListener('blur', consultarCep)