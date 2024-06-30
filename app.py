from src.assignation import Assignation
from src.reloads import Reloads


def run() -> None:
    logs = """
    2024-06-26T15:03:07.041 DEBUG [trc:arn:aws:states:us-east-1:507781971948:execution:dev3-cobis-batch-business_logic_execution_flow:476341af-ced7-44c3-8e30-f55bb82bb849|crq:af299a78-7410-4cb8-8221-223dd7ad410f|tir:BATCH|cmp:Context]
    print: BL_batch: LAZO PARA PROCESAR LAS CUENTAS DEL BLOQUE
    2024-06-26T15:03:07.042 DEBUG [trc:arn:aws:states:us-east-1:507781971948:execution:dev3-cobis-batch-business_logic_execution_flow:476341af-ced7-44c3-8e30-f55bb82bb849|crq:af299a78-7410-4cb8-8221-223dd7ad410f|tir:BATCH|cmp:Context]
    {sql:'SELECT un_cta_banco as '@w_ah_cta_banco' FROM cob_ahorros.ah_universo  WHERE (un_hilo = ? AND un_estado = 'I' AND un_intentos < ? AND un_cta_banco =  IFNULL(?, un_cta_banco)) LIMIT 1 ', prms:[1, 2, null], tm:1 ms.}
    2024-06-26T15:03:07.042 DEBUG [trc:arn:aws:states:us-east-1:507781971948:execution:dev3-cobis-batch-business_logic_execution_flow:476341af-ced7-44c3-8e30-f55bb82bb849|crq:af299a78-7410-4cb8-8221-223dd7ad410f|tir:BATCH|cmp:Context]
    print: BL_batch: <=======================================================================> PROCESANDO CUENTA: 3310017291
    2024-06-26T15:03:07.045 DEBUG [trc:arn:aws:states:us-east-1:507781971948:execution:dev3-cobis-batch-business_logic_execution_flow:476341af-ced7-44c3-8e30-f55bb82bb849|crq:af299a78-7410-4cb8-8221-223dd7ad410f|tir:BATCH|cmp:Context]
    {sql:'UPDATE cob_ahorros.ah_universo   SET un_intentos = (un_intentos + 1) WHERE (un_cta_banco = ?)', prms:[3310017291], tm:3 ms.}
    2024-06-26T15:03:07.046 DEBUG [trc:arn:aws:states:us-east-1:507781971948:execution:dev3-cobis-batch-business_logic_execution_flow:476341af-ced7-44c3-8e30-f55bb82bb849|crq:af299a78-7410-4cb8-8221-223dd7ad410f|tir:BATCH|cmp:Context]
    {sql:'SELECT  ah_fecha_ult_proceso as '@w_sig_dia', ah_cuenta as '@w_cuenta', ah_oficina as '@w_ofi', ah_estado as '@w_estado', ah_prod_banc as '@w_prod_banc', ah_moneda as '@w_moneda', ah_producto as '@w_producto' FROM cob_ahorros.ah_cuenta  WHERE (ah_cta_banco = ?)', prms:[3310017291], tm:1 ms.}
    """

    reloads = Reloads(logs)
    data = []
    for i in reloads.split_data_by_pattern():
        query, prm = i[0]
        data.append({"sql": query, "prms": prm})

    assign = Assignation()
    for i in data:
        print(assign.assignation_values(i))


if __name__ == '__main__':
    run()
