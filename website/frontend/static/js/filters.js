const currentUrl = new URL(location.toString());

const filters = (e) => {
    let parametrName = e.getAttribute('data-parametr-name');
    let parametrValue = e.getAttribute('data-parametr-value');

    if (currentUrl.searchParams.has(parametrName) && parametrValue == localStorage.getItem(parametrName)) {

        if (currentUrl.searchParams.get(parametrName)[0] == "+" ) {
            currentUrl.searchParams.set(parametrName, "-" + parametrValue);
        } else {
            currentUrl.searchParams.set(parametrName, "+" + parametrValue);            
        }

    } else {
        currentUrl.searchParams.set(parametrName, "+" + parametrValue);
    }    

    location.assign(currentUrl.href);

    savedParametrValue(parametrName, parametrValue);
}

const savedParametrValue = (parametrName, parametrValue) => {
    localStorage.setItem(parametrName, parametrValue) 
}