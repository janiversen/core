"""AEMET OpenData.

    This file is based on the generated API which AEMET provides through
    use of swagger. File is adapted to work with HA.
    
    The names and comments are in Spanish, after all this is the spanish
    institute, for that reason codespell is disabled for this file.
"""
# cSpell:disable
# spell-checker: disable
# spellchecker: disable
# coding: utf-8
"""
    AEMET OpenData es una API REST desarrollado por AEMET que permite la
    difusión y la reutilización de la información meteorológica y climatológica
    de la Agencia, en el sentido indicado en la Ley 18/2015, de 9 de julio,
    por la que se modifica la Ley 37/2007, de 16 de noviembre, sobre
    reutilización de la información del sector público.
    (IMPORTANTE: Para poder realizar peticiones, es necesario introducir en API
    Key haciendo clic en el círculo rojo de recurso REST).

    OpenAPI spec version: 2.0
"""

from .aemetClient import aemetClient


class aemetMethods(aemetClient):
    """Class with methods to access AEMET data."""

    async def __init__(self, apiKey):
        """Initialize."""
        aemetClient.__init__(apiKey)

    async def avisos_de_fenmenos_meteorolgicos_adversos__archivo(
        self, fecha_ini_str, fecha_fin_str
    ):
        """Avisos de Fenómenos Meteorológicos Adversos. Archivo.

        Avisos de Fenómenos Meteorológicos adversos para el rango de fechas
        seleccionado (datos desde 18/06/2018).

        :param str fecha_ini_str: Fecha Inicial (AAAA-MM-DDTHH:MM:SSUTC)
        :param str fecha_fin_str: Fecha Final (AAAA-MM-DDTHH:MM:SSUTC)
        """
        url = (
            "/api/avisos_cap/archivo/fechaini/"
            + fechaIniStr
            + "/fechafin/"
            + fechaFinStr
        )
        return self.request(url)

    async def avisos_de_fenmenos_meteorolgicos_adversos__ltimo_(self, area):
        """Avisos de Fenómenos Meteorológicos Adversos. Último.

        Últimos Avisos de Fenómenos Meteorológicos adversos elaborado para el
        área seleccionada.

        :param async_req bool
        :param str area: Código Área
            esp -> España
            61  -> Andalucía
            62  -> Aragón
            63  -> Asturias, Principado de
            64  -> Ballears, Illes
            78  -> Ceuta
            65  -> Canarias
            66  -> Cantabria
            67  -> Castilla y León
            68  -> Castilla - La Mancha
            69  -> Cataluña
            77  -> Comunitat Valenciana
            70  -> Extremadura
            71  -> Galicia
            72  -> Madrid, Comunidad de
            79  -> Melilla
            73  -> Murcia, Región de
            74  -> Navarra, Comunidad Foral de
            75  -> País Vasco
            76  -> Rioja, La
        """
        url = "/api/avisos_cap/ultimoelaborado/area/" + area
        return self.request(url)

    async def mapa_de_niveles_de_riesgo_estimado_meteorolgico_de_incendios_forestales_(
        self, area
    ):
        """Mapa de niveles de riesgo estimado de incendios forestales.

        Último mapa elaborado de niveles de riesgo estimado meteorológico de
        incendios forestales para el área pasada por parámetro.

        :param str area: Código Área
            p -> Península
            b -> Baleares
            c -> Canarias
        """
        url = "/api/incendios/mapasriesgo/estimado/area/" + area
        return request(url)

    async def mapa_de_niveles_de_riesgo_previsto_meteorolgico_de_incendios_forestales_(
        self, dia, area
    ):
        """Mapa de niveles de riesgo previsto de incendios forestales.

        Mapa elaborado de niveles de riesgo estimado meteorológico de incendios
        forestales para el día y el área pasados por parámetro.

        :param str dia: Código Día
            1 -> Mañana
            2 -> Pasado Mañana
            3 -> Dentro de 3 días
        :param str area: Código Área
            p -> Península
            b -> Baleares
            c -> Canarias
        """
        url = "/api/incendios/mapasriesgo/previsto/dia/{dia}/area/" + area
        return self.request(url)

    async def ndice_normalizado_de_vegetacin_(self):
        """Índice normalizado de vegetación.

        Esta imagen se realiza con una combinación de los datos del canal
        visible y del infrarrojo cercano del satélite NOAA-19, que nos da una
        idea del desarrollo de la vegetación. Esto es así debido a que la
        vegetación absorbe fuertemente la radiación del canal visible, pero
        refleja fuertemente la del infrarrojo cercano. Esta imagen se renueva
        los jueves a última hora y contiene los datos acumulados de la última
        semana.
        """
        url = "/api/satelites/producto/nvdi"
        return self.request(url)

    async def temperatura_del_agua_del_mar_(self):
        """Temperatura del agua del mar.

        Imagen obtenida con una combinación de los datos de los canales
        infrarrojos del satélite NOAA-19, que nos da la temperatura de la
        superficie del mar. Esta imagen se renueva todos los días a última
        hora y contiene los datos acumulados de los últimos siete días.
        """
        url = "/api/satelites/producto/sst"
        return self.request(url)

    async def get_municipio_using_get(self, municipio):
        """getMunicipio.

        Retorna información específica del municipio de España que se le pasa
        como parámetro.

        :param str municipio: Municipio
        """
        url = "/api/maestro/municipio/" + municipio

    async def get_municipios_using_get(self):
        """getMunicipios.

        Retorna todos los municipios de España. Este servicio es útil para
        obtener información para utilizar otros elementos de AEMET OpenData,
        como por ejemplo, la predicción de municipios para 7 días o por horas
        ya que nos retorna el id del municipio que necesitamos.
        """
        url = "/api/maestro/municipios"
        return self.request(url)

    async def mapas_de_anlisis__ltima_pasada_(self):
        """Mapas de análisis. Última pasada.

        Estos mapas muestran la configuración de la presión en superficie
        usando isobaras (lineas de igual presión), áreas de alta (A, a) y
        baja (B, b) presión y los frentes en Europa y el Atlántico Norte. El
        mapa de análisis presenta el estado de la atmósfera a la hora
        correspondiente y los fenómenos más relevantes observados en España.
        Periodicidad de actualización: cada 12 horas (00, 12).
        """
        url = "/api/mapasygraficos/analisis"
        return self.request(url)

    async def mapas_significativos__tiempo_actual_(self, fecha, ambito, dia):
        """Mapas significativos. Tiempo actual.

        Mapas significativos de ámbito nacional o CCAA, para una fecha dada y
        ese mismo día (D+0), al día siguiente (D+1) o a los dos días (D+2), en
        el periodo horario de (00_12) ó (12-24).

        :param str fecha: Fecha de elaboración (AAAA-MM-DD)
        :param str ambito: Código Ámbito
            esp -> España
            and -> Andalucía
            arn -> Aragón
            ast -> Asturias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La
        :param str dia: Código de día
            a -> D+0 (00-12)
            b -> D+0 (00-12)
            c -> D+1 (00-12)
            d -> D+1 (12-24)
            e -> D+2 (00-12)
            f -> D+2 (12-24)
        """
        url = (
            "/api/mapasygraficos/mapassignificativos/fecha/"
            + fecha
            + "/"
            + ambito
            + "/"
            + dia
        )
        return self.request(url)

    async def mapas_significativos__tiempo_actual_1(self, ambito, dia):
        """Mapas significativos. Tiempo actual.

        Mapas significativos de ámbito nacional o CCAA, para el día actual
        (D+0), al día siguiente (D+1) o a los dos días (D+2), en el periodo
        horario de (00_12) ó (12-24).

        :param str ambito: Código Ámbito
            esp -> España
            and -> Andalucía
            arn -> Aragón
            ast -> Asturias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La
        :param str dia: Código de día
            a -> D+0 (00-12)
            b -> D+0 (00-12)
            c -> D+1 (00-12)
            d -> D+1 (12-24)
            e -> D+2 (00-12)
            f -> D+2 (12-24)
        """
        url = "/api/mapasygraficos/mapassignificativos/" + ambito + "/" + dia
        return self.request(url)

    async def datos_de_observacin__tiempo_actual_(self):
        """Datos de observación. Tiempo actual.

        Datos de observación horarios de las últimas 24 horas todas las
        estaciones meteorológicas de las que se han recibido datos en ese
        período. Frecuencia de actualización: continuamente.
        """
        url = "/api/observacion/convencional/todas"
        return self.request(url)

    async def datos_de_observacin__tiempo_actual_1(self, idema):
        """Datos de observación. Tiempo actual.

        Datos de observación horarios de las últimas 24 horas de la estación
        meterológica que se pasa como parámetro (idema).
        Frecuencia de actualización: continuamente.

        :param str idema: Índicativo climatológico de la EMA
        """
        url = "/api/observacion/convencional/datos/estacion/" + idema
        return self.request(url)

    async def mensajes_de_observacin__ltimo_elaborado_(self, tipomensaje):
        """Mensajes de observación. Último elaborado.

        Últimos mensajes de observación. Para los SYNOP y TEMP devuelve los
        mensajes de las últimas 24 horas y para los CLIMAT de los 40 últimos
        dias. Se pasa como parámetro el tipo de mensaje que se desea
        (tipomensaje). El resultado de la petición es un fichero en formato
        tar.gz, que contiene los boletines en formato json y bufr.

        :param str tipomensaje: Código Tipo de Mensaje
            climat -> CLIMAT
            synop  -> SYNOP
            temp  -> TEMP  
        """
        url = "/api/observacion/convencional/mensajes/tipomensaje/" + tipomensaje
        return self.request(url)

    async def prediccin_martima_costera_(self, costa):
        """Predicción marítima costera.

        Predicción para un periodo de 24 horas de las condiciones
        meteorológicas para la zona costera pasada por parámetro.

        :param str costa: Código Área Costera
            42 -> Costa de Andalucía Occidental y Ceuta
            47 -> Costa de Andalucía Oriental y Melilla
            41 -> Costa de Asturias, Cantabria y País Vasco
            45 -> Costa de Cataluña
            40 -> Costa de Galicia
            44 -> Costa de Illes Balears
            43 -> Costa de las Islas Canarias
            46 -> Costa de Valencia y Murcia
        """
        url = "/api/prediccion/maritima/costera/costa/" + costa
        return self.request(url)

    async def prediccin_martima_de_alta_mar_(self, area):
        """Predicción marítima de alta mar.

        Predicción para un periodo de 24 horas de las condiciones
        meteorológicas para el área marítima pasada por parámetro.

        :param str area: Código Área de Alta Mar
            0 -> Océano Atlántico al sur de 35º N
            1 -> Océano Atlántico al norte de 30º N
            2 -> Mar Mediterráneo
        """
        url = "/api/prediccion/maritima/altamar/area/" + area
        return self.request(url)

    async def informacion_nivologica_(self, area):
        """Información nivológica.

        Información nivológica para la zona montañosa que se pasa como
        parámetro (area).

        :param str area: Código de Área Montañosa
            0 -> Pirineo Catalán
            1 -> Pirineo Navarro y Aragonés
        """
        url = "/api/prediccion/especifica/nivologica/" + area
        return self.request(url)

    async def prediccin_de_montaa__tiempo_actual_(self, area, dia):
        """Predicción de montaña. Tiempo actual.

        Predicción meteorológica para la zona montañosa que se pasa como
        parámetro (area) con validez para el día (día).  Periodicidad de
        actualización: continuamente.

        :param str area: Código de Área Montañosa
            peu1 -> Picos de Europa
            nav1 -> Pirineo Navarro
            arn1 -> Pirineo Aragonés
            cat1 -> Pirineo Catalán
            rio1 -> Ibérica Riojana
            arn2 -> Ibérica Aragonesa
            mad2 -> Sierras de Guadarrama y Somosierra
            gre1 -> Sierra de Gredos
            nev1 -> Sierra Nevada
        :param str dia: Código de día
            0 -> día actual
            1 -> d+1 (mañana)
            2 -> d+2 (pasado mañana)
            3 -> d+3 (siguente a pasado mañana)
        """
        url = "/api/prediccion/especifica/montaña/pasada/area/{area}/dia/" + dia
        return self.request(url)

    async def prediccin_de_montaa__tiempo_pasado_(self, area):
        """Predicción de montaña. Tiempo pasado.

        Breve resumen con lo más significativo de las condiciones
        meteorológicas registradas en la zona de montaña que se pasa como
        parámetro (area) en las últimas 24-36 horas.

        :param str area: Código de Área Montañosa 
            peu1 -> Picos de Europa
            nav1 -> Pirineo Navarro
            arn1 -> Pirineo Aragonés
            cat1 -> Pirineo Catalán
            rio1 -> Ibérica Riojana
            arn2 -> Ibérica Aragonesa
            mad2 -> Sierras de Guadarrama y Somosierra
            gre1 -> Sierra de Gredos
            nev1 -> Sierra Nevada
        """
        url = "/api/prediccion/especifica/montaña/pasada/area/" + area
        return self.request(url)

    async def prediccin_de_radiacin_ultravioleta__uvi_(self, dia):
        """Predicción de radiación ultravioleta (UVI).

         Predicción de Índice de radiación UV máximo en condiciones de cielo
        despejado para el día seleccionado.

        :param str dia: Código de día
            0 -> día actual
            1 -> d+1 (mañana)
            2 -> d+2 (pasado mañana)
            3 -> d+3 (dentro de 3 días)
            4 -> d+4 (dentro de 4 días)
        """
        url = "/api/prediccion/especifica/uvi/" + dia
        return self.request(url)

    async def prediccin_para_las_playas__tiempo_actual_(self, playa):
        """Predicción para las playas. Tiempo actual.

        La predicción diaria de la playa que se pasa como parámetro. Establece
        el estado de nubosidad para unas horas determinadas, las 11 y las 17
        hora oficial. Se analiza también si se espera precipitación en el
        entorno de esas horas, entre las 08 y las 14 horas y entre las 14 y 20
        horas.

        :param str playa: Código de playa
            http://www.aemet.es/documentos/es/eltiempo/prediccion/playas/Playas_codigos.csv
        """
        url = "/api/prediccion/especifica/playa/" + playa
        return self.request(url)

    async def prediccin_por_municipios_diaria__tiempo_actual_(self, municipio):
        """Predicción por municipios diaria. Tiempo actual.

        Predicción para el municipio que se pasa como parámetro (municipio).
        Periodicidad de actualización: continuamente.

        :param str municipio: Código de municipio
            http://www.ine.es/daco/daco42/codmun/codmunmapa.htm
        """
        url = "/api/prediccion/especifica/municipio/diaria/" + municipio
        return self.request(url)

    async def prediccin_por_municipios_horaria__tiempo_actual_(self, municipio):
        """Predicción por municipios horaria. Tiempo actual.

        Predicción horaria para el municipio que se pasa como parámetro
        (municipio). Presenta la información de hora en hora hasta 48 horas.

        :param str municipio: Código de municipio
            http://www.ine.es/daco/daco42/codmun/codmunmapa.htm
        """
        url = "/api/prediccion/especifica/municipio/horaria/" + municipio
        return self.request(url)

    async def prediccin_ccaa_hoy__archivo_(self, ccaa, fecha):
        """Predicción CCAA hoy. Archivo.

        Predicción para la comunidad autónoma que se pasa como parámetro (ccaa)
        con validez para el día de fecha de elaboración que se pasa como
        parámetro (fecha). Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La   
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        url = "/api/prediccion/ccaa/hoy/" + ccaa + "/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_ccaa_hoy__tiempo_actual_(self, ccaa):
        """Predicción CCAA hoy. Tiempo actual.

        Predicción para la CCAA que se pasa como parámetro con validez para
        mismo día que la fecha de petición. En el caso de que en la fecha de
        petición este producto todavía no se hubiera elaborado, se retornará el
        último elaborado. Actualización continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Asturias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La
        """
        url = "/api/prediccion/ccaa/hoy/" + ccaa
        return self.request(url)

    async def prediccin_ccaa_maana__archivo_(self, ccaa, fecha):
        """Predicción CCAA mañana. Archivo.

        Predicción para la comunidad autónoma que se pasa como parámetro (ccaa)
        con validez para el día siguiente a la fecha de elaboración que se pasa
        como parámetro (fecha). Periodicidad de actualización. continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La   
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        url = "/api/prediccion/ccaa/manana/" + ccaa + "/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_ccaa_maana__tiempo_actual_(self, ccaa):
        """Predicción CCAA mañana. Tiempo actual.

        Predicción para la comunidad autónoma que se pasa como parámetro para
        el día siguiente a la fecha de la petición. En el caso de el producto
        no se hubiera elaborado todavía en la fecha de petición se retornará el
        último producto elaborado.
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La   
        """
        url = "/api/prediccion/ccaa/manana/" + ccaa
        return self.request(url)

    async def prediccin_ccaa_medio_plazo__archivo_(self, ccaa, fecha):
        """Predicción CCAA medio plazo. Archivo.

        Predicción de mediio plazo para la comunidad autónoma que se pasa como
        parámetro (ccaa) a partir de la fecha de elaboración que se pasa como
        parámetro (fecha). Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La   
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        url = "/api/prediccion/ccaa/medioplazo/" + ccaa + "/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_ccaa_medio_plazo__tiempo_actual_(self, ccaa):
        """Predicción CCAA medio plazo. Tiempo actual.

        Predicción para la comunidad autónoma que se pasa como parámetro (ccaa)
        y con validez para el medio plazo a partir de la fecha de petición. En
        el caso de que en el fecha de la petición no se hubiera generado aún el
        producto, se retornará el última elaborado.
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La
        """
        url = "/api/prediccion/ccaa/medioplazo/" + ccaa
        return self.request(url)

    async def prediccin_ccaa_pasado_maana__archivo_(self, ccaa, fecha):
        """Predicción CCAA pasado mañana. Archivo.

        Predicción para la comunidad autónoma que se pasa como parámetro (ccaa)
        y validez para pasado mañana a partir de la fecha de elaboración que se
        pasa como parámetro (fecha).
        Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        url = "/api/prediccion/ccaa/pasadomanana/" + ccaa + "/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_ccaa_pasado_maana__tiempo_actual_(self, ccaa):
        """Predicción CCAA pasado mañana. Tiempo actual.

        Predicción para la comunidad autónoma que se pasa como parámetro (ccaa)
        y validez para el medio plazo a partir de la fecha de la petición. En
        el caso de que en la fecha de la petición dicho producto aún no se
        hubiera generado retornará el último de este tipo que se hubiera
        generado.  Periodicidad de actualización: continuamente.

        :param str ccaa: Código de CCAA
            and -> Andalucía
            arn -> Aragón
            ast -> Astrrias
            bal -> Ballears, Illes
            coo -> Canarias
            can -> Cantabria
            cle -> Castilla y León
            clm -> Castilla - La Mancha
            cat -> Cataluña
            val -> Comunitat Valenciana
            ext -> Extremadura
            gal -> Galicia
            mad -> Madrid, Comunidad de
            mur -> Murcia, Región de
            nav -> Navarra, Comunidad Foral de
            pva -> País Vasco
            rio -> Rioja, La
        """
        url = "/api/prediccion/ccaa/pasadomanana/" + ccaa
        return self.request(url)

    async def prediccin_nacional_hoy__archivo_(self, fecha):
        """Predicción nacional hoy. Archivo.

        Predicción nacional para el día correspondiente a la fecha que se pasa
        como parámetro en en formato texto. Actualización diaria. Hay días en
        los que este producto no se realiza. En ese caso se devuelve un 404
        producto no existente.

        :param str fecha: Fecha en formato (AAAA-MM-DD)
        """
        url = "/api/prediccion/nacional/hoy/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_nacional_hoy__tiempo_actual_(self):
        """Predicción nacional hoy. Última elaborada.

        Predicción nacional para el día actual a la fecha de elaboración en
        formato texto. Actualización diaria. Hay días en los que este producto
        no se realiza. En ese caso se devuelve la predicción nacional última
        que se elaboró.
        """
        url = "/api/prediccion/nacional/hoy"
        return self.request(url)

    async def prediccin_nacional_maana__archivo_(self, fecha):
        """Predicción nacional mañana. Archivo.

        Predicción nacional para el día siguiente a la fecha de elaboración. En
        este caso la fecha de elaboración es la fecha que se pasa como
        parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        url = "/api/prediccion/nacional/manana/elaboracion/{fecha}"
        return self.request(url)

    async def prediccin_nacional_maana__tiempo_actual_(self):
        """Predicción nacional mañana. Tiempo actual.

        Predicción nacional para el día siguiente a la fecha de elaboración. En
        este caso la fecha de elaboración es el día actual. Actualización
        diaria. En el caso de que en el día actual  todavía no se haya
        elaborado se devolverá el último producto de predicción nacional para
        mañana elaborado.
        """
        url = "/api/prediccion/nacional/manana"
        return self.request(url)

    async def prediccin_nacional_medio_plazo__archivo_(self, fecha):
        """Predicción nacional medio plazo. Archivo.

        Predicción nacional para el medio plazo siguiente a la fecha de
        elaboración. En este caso, la fecha de elaboración es la fecha que se
        pasa como parámetro. Actualización diaria.
 
        :param str fecha: Día (AAAA-MM-DD)
        """
        url = "/api/prediccion/nacional/medioplazo/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_nacional_medio_plazo__tiempo_actual_(self):
        """Predicción nacional medio plazo. Tiempo actual.

        Predicción nacional para medio plazo siguiente a la fecha de
        elaboración. En este caso la fecha de elaboración es el día actual.
        Actualización diaria. En el caso de que en el día actual  todavía no se
        haya elaborado se devolverá el último producto de predicción nacional
        para medio plazo elaborado.
        """
        url = "/api/prediccion/nacional/medioplazo"
        return self.request(url)

    async def prediccin_nacional_pasado_maana__archivo_(self, fecha):
        """Predicción nacional pasado mañana. Archivo.

        Predicción nacional para pasado mañana siguiente a la fecha de
        elaboración. En este caso, la fecha de elaboración es la fecha que se
        pasa como parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        url = "/api/prediccion/nacional/pasadomanana/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_nacional_pasado_maana__tiempo_actual_(self):
        """Predicción nacional pasado mañana. Tiempo actual.

        Predicción nacional para pasado mañana siguiente a la fecha de
        elaboración. En este caso la fecha de elaboración es el día actual.
        Actualización diaria. En el caso de que en el día actual  todavía no se
        haya elaborado se devolverá el último producto de predicción nacional
        para pasado mañana elaborado.
        """
        url = "/api/prediccion/nacional/pasadomanana"
        return self.request(url)

    async def prediccin_nacional_tendencia__archivo_(self, fecha):
        """Predicción nacional tendencia. Archivo.

        Predicción nacional para tendencia siguiente a la fecha de elaboración.
        En este caso, la fecha de elaboración es la fecha que se pasa como
        parámetro. Actualización diaria.

        :param str fecha: Día (AAAA-MM-DD)
        """
        url = "/api/prediccion/nacional/tendencia/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_nacional_tendencia__tiempo_actual_(self):
        """Predicción nacional tendencia. Tiempo actual.

        Predicción nacional para tendencia siguiente a la fecha de elaboración.
        En este caso la fecha de elaboración es el día actual. Actualización
        diaria. En el caso de que en el día actual  todavía no se haya
        elaborado se devolverá el último producto de predicción nacional para
        tendencia elaborado.
        """
        url = "/api/prediccion/nacional/tendencia"
        return self.request(url)

    async def prediccin_provincia_hoy__archivo_(self, provincia, fecha):
        """Predicción provincia hoy. Archivo.

        Predicción del día siguiente a la fecha que se pasa como parámetro para
        la provincia que se pasa como parámetro. Actualización continua y fija
        a las 14:00 Hora Oficial Peninsular del día que se pasa como parámetro.

        :param str provincia: Código Provincia
            01 -> Araba/Álava
            02 -> Albacete
            03 -> Alacant/Alicante
            04 -> Almería
            33 -> Asturias
            05 -> Ávila
            06 -> Badajoz
            07 -> Illes Ballears
            08 -> Barcelona
            48 -> Bizkaia
            09 -> Burgos
            10 -> Cáceres
            11 -> Cádiz
            39 -> Cantabria
            12 -> Castelló/Castellón
            51 -> Ceuta
            13 -> Ciudad Real
            14 -> Córdoba
            15 -> A Coruña
            16 -> Cuenca
            17 -> Girona
            18 -> Granada
            19 -> Guadalajara
            20 -> Gipuzkoa
            21 -> Huelva
            22 -> Huesca
            23 -> Jaén
            24 -> León
            25 -> Lleida
            27 -> Lugo
            28 -> Madrid
            29 -> Málaga
            52 -> Melilla
            30 -> Murcia
            31 -> Navarra
            32 -> Oursense
            34 -> Palencia
            35 -> Las Palmas
            36 -> Pontevedra
            26 -> La Rioja
            37 -> Salamanca
            38 -> Santa Cruz de Tenerife
            40 -> Segovia
            41 -> Sevilla
            42 -> Soria
            43 -> Tarragona
            44 -> Teruel
            45 -> Toledo
            46 -> València/Valencia
            47 -> Valladolid
            49 -> Zamora
            50 -> Zaragoza 
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        url = "/api/prediccion/provincia/hoy/" + provincia + "/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_provincia_hoy__tiempo_actual_(self, provincia):
        """Predicción provincia hoy. Tiempo actual.

        Predicción del día actual para la provincia que se pasa como parámetro.
        En el caso de que este producto no se haya elaborado todavía en el día
        actual, se retorna el último elaborado. Actualización continua y fija a
        las 14:00 Hora Oficial Peninsular.

        :param str provincia: Código Provincia
            01 -> Araba/Álava
            02 -> Albacete
            03 -> Alacant/Alicante
            04 -> Almería
            33 -> Asturias
            05 -> Ávila
            06 -> Badajoz
            07 -> Illes Ballears
            08 -> Barcelona
            48 -> Bizkaia
            09 -> Burgos
            10 -> Cáceres
            11 -> Cádiz
            39 -> Cantabria
            12 -> Castelló/Castellón
            51 -> Ceuta
            13 -> Ciudad Real
            14 -> Córdoba
            15 -> A Coruña
            16 -> Cuenca
            17 -> Girona
            18 -> Granada
            19 -> Guadalajara
            20 -> Gipuzkoa
            21 -> Huelva
            22 -> Huesca
            23 -> Jaén
            24 -> León
            25 -> Lleida
            27 -> Lugo
            28 -> Madrid
            29 -> Málaga
            52 -> Melilla
            30 -> Murcia
            31 -> Navarra
            32 -> Oursense
            34 -> Palencia
            35 -> Las Palmas
            36 -> Pontevedra
            26 -> La Rioja
            37 -> Salamanca
            38 -> Santa Cruz de Tenerife
            40 -> Segovia
            41 -> Sevilla
            42 -> Soria
            43 -> Tarragona
            44 -> Teruel
            45 -> Toledo
            46 -> València/Valencia
            47 -> Valladolid
            49 -> Zamora
            50 -> Zaragoza 
        """
        url = "/api/prediccion/provincia/hoy/" + provincia
        return self.request(url)

    async def prediccin_provincia_maana__archivo_(self, provincia, fecha):
        """Predicción provincia mañana. Archivo.

        Predicción del día siguiente a la fecha que se pasa como parámetro para
        la provincia que se pasa como parámetro. Actualización continua y fija
        a las 14:00 Hora Oficial Peninsular del día que se pasa como parámetro.

        :param str provincia: Código Provincia
            01 -> Araba/Álava
            02 -> Albacete
            03 -> Alacant/Alicante
            04 -> Almería
            33 -> Asturias
            05 -> Ávila
            06 -> Badajoz
            07 -> Illes Ballears
            08 -> Barcelona
            48 -> Bizkaia
            09 -> Burgos
            10 -> Cáceres
            11 -> Cádiz
            39 -> Cantabria
            12 -> Castelló/Castellón
            51 -> Ceuta
            13 -> Ciudad Real
            14 -> Córdoba
            15 -> A Coruña
            16 -> Cuenca
            17 -> Girona
            18 -> Granada
            19 -> Guadalajara
            20 -> Gipuzkoa
            21 -> Huelva
            22 -> Huesca
            23 -> Jaén
            24 -> León
            25 -> Lleida
            27 -> Lugo
            28 -> Madrid
            29 -> Málaga
            52 -> Melilla
            30 -> Murcia
            31 -> Navarra
            32 -> Oursense
            34 -> Palencia
            35 -> Las Palmas
            36 -> Pontevedra
            26 -> La Rioja
            37 -> Salamanca
            38 -> Santa Cruz de Tenerife
            40 -> Segovia
            41 -> Sevilla
            42 -> Soria
            43 -> Tarragona
            44 -> Teruel
            45 -> Toledo
            46 -> València/Valencia
            47 -> Valladolid
            49 -> Zamora
            50 -> Zaragoza 
        :param str fecha: Día de elaboración (AAAA-MM-DD)
        """
        url = "/api/prediccion/provincia/manana/" + provincia + "/elaboracion/" + fecha
        return self.request(url)

    async def prediccin_provincia_maana__tiempo_actual_(self, provincia):
        """Predicción provincia mañana. Tiempo actual.

        Predicción del día siguiente para la provincia que se pasa como
        parámetro. En el caso de que este producto no se haya elaborado todavía
        en el día actual, se retorna el último elaborado. Actualización
        continua y fija a las 14:00 Hora Oficial Peninsular.

        :param str provincia: Código Provincia
            01 -> Araba/Álava
            02 -> Albacete
            03 -> Alacant/Alicante
            04 -> Almería
            33 -> Asturias
            05 -> Ávila
            06 -> Badajoz
            07 -> Illes Ballears
            08 -> Barcelona
            48 -> Bizkaia
            09 -> Burgos
            10 -> Cáceres
            11 -> Cádiz
            39 -> Cantabria
            12 -> Castelló/Castellón
            51 -> Ceuta
            13 -> Ciudad Real
            14 -> Córdoba
            15 -> A Coruña
            16 -> Cuenca
            17 -> Girona
            18 -> Granada
            19 -> Guadalajara
            20 -> Gipuzkoa
            21 -> Huelva
            22 -> Huesca
            23 -> Jaén
            24 -> León
            25 -> Lleida
            27 -> Lugo
            28 -> Madrid
            29 -> Málaga
            52 -> Melilla
            30 -> Murcia
            31 -> Navarra
            32 -> Oursense
            34 -> Palencia
            35 -> Las Palmas
            36 -> Pontevedra
            26 -> La Rioja
            37 -> Salamanca
            38 -> Santa Cruz de Tenerife
            40 -> Segovia
            41 -> Sevilla
            42 -> Soria
            43 -> Tarragona
            44 -> Teruel
            45 -> Toledo
            46 -> València/Valencia
            47 -> Valladolid
            49 -> Zamora
            50 -> Zaragoza 
        """
        url = "/api/prediccion/provincia/manana/" + provincia
        return self.request(url)

    async def balance_hdrico_nacional__documento_(self, anio, decena):
        """Balance hídrico nacional (documento).

        Se obtiene, para la decema y el año pasados por parámetro, el Boletín
        Hídrico Nacional que se elabora cada diez días. Se presenta información
        resumida de forma distribuida para todo el territorio nacional de
        diferentes variables, en las que se incluye informaciones de la
        precipitación y la evapotranspiración potencial acumuladas desde el 1
        de septiembre.

        :param str anio: Año (AAAA)
        :param str decena: Decena de 01 (primera decena) a 36 (última decena)
        """
        url = "/api/productos/climatologicos/balancehidrico/" + anio + "/" + decena
        return self.request(url)

    async def capas_shape_de_estaciones_climatolgicas_(self, tipoestacion):
        """Capas SHAPE de estaciones climatológicas de AEMET.

        Capas SHAPE de las distintas estaciones climatológicas de AEMET:
        automáticas, completas, pluviométricas y termométricas.
 
        :param str tipoestacion: Código Tipo de Estación
            automaticas    -> Estaciones Automáticas
            completas      -> Estaciones Completas
            pluviometricas -> Estaciones Pluviométricas
            termometricas  -> Estaciones Termométricas   
        """
        url = "/api/productos/climatologicos/capasshape/" + tipoestacion
        return self.request(url)

    async def resumen_mensual_climatolgico_nacional__documento_(self, anio, mes):
        """Resumen mensual climatológico nacional (documento).

        Resumen climatológico nacional, para el año y mes pasado por parámetro,
        sobre el estado del clima y la evolución de las principales variables
        climáticas, en especial temperatura y precipitación, a nivel mensual,
        estacional y anual.

        :param str anio: Año (AAAA)
        :param str mes: Mes (mm)
        """
        url = (
            "/api/productos/climatologicos/resumenclimatologico/nacional/"
            + anio
            + "/"
            + mes
        )
        return self.request(url)

    async def imagen_composicin_nacional_radares__tiempo_actual_estndar_(self):
        """Imagen composición nacional radares. Tiempo actual estándar.

        Imagen composición nacional radares. Tiempo actual estándar.
        Periodicidad: 30 minutos.
        """
        url = "/api/red/radar/nacional"
        return self.request(url)

    async def radar_regional(self, radar):
        """Imagen gráfica radar regional. Tiempo actual estándar.

        Imagen del radar regional de la región pasada por parámetro. Tiempo
        actual estándar. Periodicidad: 10 minutos.

        :param str radar: Código Radar
            am -> Almería
            sa -> Asturias
            pm -> Illes Balears
            ba -> Barcelona
            cc -> Cáceres
            co -> A Coruña
            ma -> Madrid
            ml -> Málaga
            mu -> Murcia
            vd -> Palencia
            ca -> Las Palmas
            se -> Sevilla
            va -> Valencia
            ss -> Vizcaya
            za -> Zaragoza   
        """
        url = "/api/red/radar/regional/" + radar
        return self.request(url)

    async def mapa_con_los_rayos_registrados_en_periodo_standard__ltimo_elaborado_(
        self,
    ):
        """Mapa con los rayos registrados en periodo standard. Último elaborado.

        Imagen de las descargas caídas en el territorio nacional durante un
        período de 12 horas.
        """
        url = "/api/red/rayos/mapa"
        return self.request(url)

    async def contenido_total_de_ozono__tiempo_actual_(self):
        """Contenido total de ozono. Tiempo actual.

        Dato medio diario de contenido total de ozono. Cada 24 h (actualmente,
        en fines de semana, festivos y vacaciones no se genera por la falta de
        personal en el Centro Radiométrico Nacional).
        """
        url = "/api/red/especial/ozono"

    async def datos_de_contaminacin_de_fondo__tiempo_actual_(self, nombre_estacion):
        """Datos de contaminación de fondo. Tiempo actual.

        Ficheros diarios con datos diezminutales de la estación de la red de
        contaminación de fondo EMEP/VAG/CAMP pasada por parámetro, de
        temperatura, presión, humedad, viento (dirección y velocidad),
        radiación global, precipitación y 4 componentes químicos: O3,SO2,NO,NO2
        y PM10. Los datos se encuentran en formato FINN (propio del Ministerio
        de Medio Ambiente). Periodicidad: cada hora.

        :param str nombre_estacion: Código Estación de la Red EMEP
            11 -> Barcarrota (Badajoz)
            10 -> Cabo de Creus (Girona)
            09 -> Campisábalos (Guadalajara)
            17 -> Doñana (Huelva)
            14 -> Els Torms (Lleida)
            06 -> Mahón (Illes Balears)
            08 -> Niembro-Llanes (Asturias)
            05 -> Noia (A Coruña)
            16 -> O Saviñao (Lugo)
            13 -> Peñausende (Zamora)
            01 -> San Pablo de los Montes (Toledo)
            07 -> Víznar (Granada)
            12 -> Zarra (Valencia) 
        """
        url = "/api/red/especial/contaminacionfondo/estacion/" + nombre_estacion
        return self.request(url)

    async def datos_de_radiacin_global_directa_o_difusa__tiempo_actual_(self):
        """Datos de radiación global, directa o difusa. Tiempo actual.

        Datos horarios (HORA SOLAR VERDADERA) acumulados de radiación  global,
        directa, difusa e infrarroja, y datos semihorarios  (HORA SOLAR
        VERDADERA) acumulados de radiación ultravioleta eritemática.Datos
        diarios acumulados  de radiación global, directa, difusa, ultravioleta
        eritemática e infrarroja. Periodicidad: Cada 24h (actualmente en fines
        de semana, festivos y vacaciones, no se genera por la ausencia de
        personal en el Centro Radiométrico Nacional).
        """
        url = "/api/red/especial/radiacion"
        return self.request(url)

    async def perfiles_verticales_de_ozono__tiempo_actual_(self, estacion):
        """Perfiles verticales de ozono. Tiempo actual.

        Perfil Vertical de Ozono de la estación pasada por parámetro.
        Periodicidad: cada 7 días.

        :param str estacion: Código Estación
            canarias
            Izaña
            peninsula
            Madrid   
        """
        url = "/api/red/especial/perfilozono/estacion/" + estacion
        return self.request(url)

    async def climatologas_diarias_(self, fecha_ini_str, fecha_fin_str, idema):
        """Climatologías diarias.

        Valores climatológicos para el rango de fechas y la estación
        seleccionada. Periodicidad: 1 vez al día.

        :param str fecha_ini_str: Fecha Inicial (AAAA-MM-DDTHH:MM:SSUTC)
        :param str fecha_fin_str: Fecha Final (AAAA-MM-DDTHH:MM:SSUTC)
        :param str idema: Indicativo climatológico de la EMA.
            Puede introducir varios indicativos separados por comas (,)
        """
        url = (
            "/api/valores/climatologicos/diarios/datos/fechaini/"
            + fechaIniStr
            + "/fechafin/"
            + fechaFinStr
            + "/estacion/"
            + idema
        )
        return self.request(url)

    async def climatologas_diarias_1(self, fecha_ini_str, fecha_fin_str):
        """Climatologías diarias.

        Valores climatológicos de todas las estaciones para el rango de fechas
        seleccionado. Periodicidad: 1 vez al día.

        :param str fecha_ini_str: Fecha Inicial (AAAA-MM-DDTHH:MM:SSUTC)
        :param str fecha_fin_str: Fecha Final (AAAA-MM-DDTHH:MM:SSUTC)
        """
        url = (
            "/api/valores/climatologicos/diarios/datos/fechaini/"
            + fechaIniStr
            + "/fechafin/"
            + fechaFinStr
            + "/todasestaciones"
        )
        return self.request(url)

    async def climatologas_mensuales_anuales_(self, anio_ini_str, anio_fin_str, idema):
        """Climatologías mensuales anuales.

        Valores medios mensuales y anuales de los datos climatológicos para la
        estación y el periodo de años pasados por parámetro.
        Periodicidad: 1 vez al día.

        :param str anio_ini_str: Año Inicial (AAAA)
        :param str anio_fin_str: Año Final (AAAA)
        :param str idema: Indicativo climatológico de la EMA
        """
        url = (
            "/api/valores/climatologicos/mensualesanuales/datos/anioini/"
            + anioIniStr
            + "/aniofin/"
            + anioFinStr
            + "/estacion/"
            + idema
        )
        return self.request(url)

    async def climatologas_normales__19812010_(self, idema):
        """Climatologías normales (1981-2010).

        Valores climatológicos normales (periodo 1981-2010) para la estación
        pasada por parámetro. Periodicidad: 1 vez al día.

        :param str idema: Indicativo climatológico de la EMA
        """
        url = "/api/valores/climatologicos/normales/estacion/" + idema
        return self.request(url)

    async def estaciones_por_indicativo_(self, estaciones):
        """Estaciones por indicativo.

        Características de la estación climatológica pasada por parámetro.

        :param str estaciones: Listado de indicativos climatológicos
                (id1,id2,id3,...,idn)
        """
        url = (
            "/api/valores/climatologicos/inventarioestaciones/estaciones/" + estaciones
        )
        return self.request(url)

    async def inventario_de_estaciones__valores_climatolgicos_(self):
        """Inventario de estaciones (valores climatológicos).

        Inventario con las características de todas las estaciones
        climatológicas. Periodicidad: 1 vez al día.
        """
        url = "/api/valores/climatologicos/inventarioestaciones/todasestaciones"
        return self.request(url)

    async def valores_extremos_(self, parametro, idema):
        """Valores extremos.

        Valores extremos para la estación y la variable (precipitación,
        temperatura y viento) pasadas por parámetro.
        Periodicidad: 1 vez al día.

        :param str parametro: Código Parámetro Meteorológico
            P -> Precipitación
            T -> Temperatura   | | V  | Viento 
        :param str idema: Indicativo climatológico de la EMA
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.valores_extremos__with_http_info(
                parametro, idema, **kwargs
            )  # noqa: E501
        else:
            (data) = self.valores_extremos__with_http_info(
                parametro, idema, **kwargs
            )  # noqa: E501
            return data

    async def valores_extremos__with_http_info(
        self, parametro, idema, **kwargs
    ):  # noqa: E501
        """Valores extremos.  # noqa: E501

        Valores extremos para la estación y la variable (precipitación, temperatura y viento) pasadas por parámetro. Periodicidad: 1 vez al día.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.valores_extremos__with_http_info(parametro, idema, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parametro:  | Código | Parámetro Meteorológico | |----------|----------| | P  | Precipitación   | | T  | Temperatura   | | V  | Viento 
        :param str idema: Indicativo climatológico de la EMA
        :return: Model200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["parametro", "idema"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method valores_extremos_" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'parametro' is set
        if "parametro" not in params or params["parametro"] is None:
            raise ValueError(
                "Missing the required parameter `parametro` when calling `valores_extremos_`"
            )  # noqa: E501
        # verify the required parameter 'idema' is set
        if "idema" not in params or params["idema"] is None:
            raise ValueError(
                "Missing the required parameter `idema` when calling `valores_extremos_`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "parametro" in params:
            path_params["parametro"] = params["parametro"]  # noqa: E501
        if "idema" in params:
            path_params["idema"] = params["idema"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["api_key"]  # noqa: E501

        return self.api_client.call_api(
            "/api/valores/climatologicos/valoresextremos/parametro/{parametro}/estacion/{idema}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Model200",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )


# flake8: noqa
