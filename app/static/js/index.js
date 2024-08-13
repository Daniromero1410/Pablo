let dataTable;
let dataTableIsInitialized=false;


const dataTableOptions={
    columnDefs:[
        {className: 'centered', targets:[0,1,2,3,4,5,6,7,8,9,10,11]},
        {orderable: false,targets:[5,6]},
    ],
    pageLength: 4,
    destroy: true,
};
const initDataTable =async()=>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await listIngenierias();

    dataTable=$('#datatable-ingenieria').DataTable({});

    dataTableIsInitialized = true;
};

const listIngenierias = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/app/list_ingenieria/');
        const data = await response.json();

        let content = ``;
        data.Ingenieria.forEach((Ingenieria, index) => {
            content += `<tr>
                    <td>${index+1}</td>
                    <td>${Ingenieria.convocatoria}</td>
                    <td>${Ingenieria.codigo_proyecto}</td>
                    <td>${Ingenieria.nombre_proyecto}</td>
                    <td>${Ingenieria.estado}</td>
                    <td>${Ingenieria.fecha_inicio}</td>
                    <td>${Ingenieria.fecha_finalizacion}</td>
                    <td>${Ingenieria.sede}</td>
                    <td>${Ingenieria.grupo_investigacion}</td>
                    <td>${Ingenieria.programas_academicos}</td>
                    <td>${Ingenieria.investigador_principal}</td>
                    <td>${Ingenieria.coinvestigadores}</td>
                </tr>`;
        });
        tableBody_Ingenieria.innerHTML = content;

        

    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
});
