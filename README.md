# SOXMonitor
Sarbanes-Oxley Report


### Overview
La Ley Sarbanes Oxley, cuyo titulo oficial en ingles es Sarbanes-Oxley Act of 2002, Pub. L. No. 107-204,
116 Stat. 745 (30 de julio de 2002), es una ley de Estados Unidos tambien conocida como el Acta de 
Reforma de la Contabilidad Publica de Empresas y de Proteccion al Inversionista.
Tambien es llamada SOX, SarbOx o SOA.


### Options

#### Listar aplicaciones y ambientes
Se usa convencion sobre configuracion (rails mood), se especifican los ambientes por defecto con un
formato establecido.

    username $> soxmonitor --list
    SOXMonitor
    »
    Group     | Component     | Environment
    ----------+---------------+-----------------
    GPN       | DevOrder.war  | Production
    GPN       | DevOrder.war  | Development
    GPN       | DevOrder.war  | UserAcceptance
    GPN       | DevOrder.war  | Integration
    GPN       | DevOrder.war  | QAssurance
    ...


#### Reporte del grupo de aplicaciones GPN, por defecto ambiente productivo modo expandido
Por defecto se crea un reporte en modo CSV (Comma Separated Values) para integrarlo en otros documentos
con mayor facilidad, se deposita en soxmonitor/tmp/20130124-soxmonitor.csv.

    username $> soxmonitor --group=GPN --verbose
    SOXMonitor
    »
    Group       | GPN
    Environment | Production
    Hostname    | mxlinuxdo
    Address     | 10.200.60.120
    Component   | DevOrder.war
    Path        | /home/corefiles/RFC1301C2345/
    References  | /home/corefiles/DevOrder.war.CURRENT
    Permissions | -rw-------
    Date        | 24.01.2013
    Digest      | 48deb47a77863859e5bc0780b7ff6efc
    Container   | WebLogic 10.3.3
    Config      | /opt/apps/wl9mp2/bea2/projects/domains/wlsnxt/config/config.xml
    ...


#### Crear un reporte de la aplicacion GPN, del ambiente de desarrollo.

    username $> soxmonitor --group=GPN --development
    SOXMonitor
    »
    Group     | Component          | Permissions | Digest
    ----------+--------------------+-------------+----------------------------------
    GPN       | DevOrder.war       | -rw-------  | 48deb47a77863859e5bc0780b7ff6efc
    GPN       | CVD.war            | -rw-------  | ad0ecff7019dc5c90f9312a1f144cfe4
    ...


#### TODO: Reporte de la aplicacion DevOrder en todos los ambientes existentes

    username $> soxmonitor --component=DevOrder.war --all
    SOXMonitor
    »
    Component           | Date       | Environment    | Address         | Digest
    --------------------+------------+----------------+-----------------+----------------------------------
    DevOrder.war        | 24.01.2013 | Development    | 192.168.12.143  | 48deb47a77863859e5bc0780b7ff6efc
    DevOrder.war        | 10.11.2012 | Production     | 10.200.60.120   | ad0ecff7019dc5c90f9312a1f144cfe4
    DevOrder.war        | 24.01.2013 | UserAcceptance | 10.103.12.12    | 48deb47a77863859e5bc0780b7ff6efc
    ...


#### Mostrar ayuda

    username $> soxmonitor --help
    SOXMonitor
    Audit and create reports of status about your deployed components. 
    See http://github.com/andresaquino/soxmonitor
    
    This is free software; see the source for copying conditions. There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    
    Usage: soxmonitor [options] ...
        -g, --group         Group of applications
        -c, --component     An individual component, must be exists in a group
        -e, --environment   Environment, some alias was created but is possible to define new enviroments,
                            some aliases are (--prod, --dev, --int, --qa, and --uat) or in GNU mode
                            -e=production, --environment=useracceptance, -e=3gintegration
                            Can you guess why..?
        -v, --verbose       Add more information to output, additionally create a new report in vendor
                            directory
        -h, --help
            --version
    
    Report bugs to <aquino@hp.com>


#### Mostrar version

    username $> soxmonitor --version
    SOXMonitor version 0.1.1RC
    
    Developed by 
    Andres Aquino <aquino@hp.com> 


#### References

 > "Less is more" - Ludwig Mies van der Rohe
 > [from Wikipedia](http://goo.gl/eiB2b)

 > Development Environments, Software Development Process
 > [from Wikipedia](http://goo.gl/t1r4N)

 > Convention over Configuration
 > [from Wikipedia](http://goo.gl/iH5xh)

 > Markdown reference
 > [Daring Fireball](http://goo.gl/AGg1u)

```
# vim: set ts=4 sw=4 sts=4 et si ai tw=80 lbr syntax=markdown:
```
