# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps

# pylint: disable=line-too-long

helps['sql'] = """
            type: group
            short-summary: Manage databases.
            """
helps['sql db'] = """
            type: group
            short-summary: Manage databases.
            """
helps['sql db copy'] = """
            type: command
            short-summary: Creates a copy of an existing database.
            """
helps['sql db create'] = """
            type: command
            short-summary: Creates a database.
            """
helps['sql db create-replica'] = """
            type: command
            short-summary: Creates a readable secondary replica of an existing database.
            """
helps['sql db delete'] = """
            type: command
            short-summary: Deletes a database.
            """
helps['sql db list'] = """
            type: command
            short-summary: Lists all databases in a server, or all databases in an elastic pool.
            """
helps['sql db update'] = """
            type: command
            short-summary: Updates a database.
            """
helps['sql db replica-link'] = """
            type: group
            short-summary: Manage links between database replicas.
            """
# helps['sql db data-warehouse'] = """
#             type: group
#             short-summary: Manage database data warehouse.
#             """
# helps['sql db restore-point'] = """
#             type: group
#             short-summary: Manage database restore points.
#             """
# helps['sql db transparent-data-encryption'] = """
#             type: group
#             short-summary: Manage database transparent data encryption.
#             """
# helps['sql db service-tier-advisor'] = """
#             type: group
#             short-summary: Manage database service tier advisors.
#             """
helps['sql elastic-pool'] = """
            type: group
            short-summary: Manage elastic pools. An elastic pool is an allocation of CPU, IO, and memory resources. Databases inside the pool share these resources.
            """
helps['sql elastic-pool create'] = """
            type: command
            short-summary: Creates an elastic pool.
            """
helps['sql elastic-pool update'] = """
            type: command
            short-summary: Updates an elastic pool.
            """
# helps['sql elastic-pool recommended'] = """
#             type: group
#             short-summary: Manages recommended elastic pools.
#             """
# helps['sql elastic-pool recommended db'] = """
#             type: group
#             short-summary: Manage recommended elastic pool databases.
#             """
helps['sql server'] = """
            type: group
            short-summary: Manage servers.
            """
helps['sql server create'] = """
            type: command
            short-summary: Creates a server.
            """
helps['sql server list'] = """
            type: command
            short-summary: Lists servers.
            """
helps['sql server update'] = """
            type: command
            short-summary: Updates a server.
            """
helps['sql server firewall-rule'] = """
            type: group
            short-summary: Manage a server's firewall rules.
            """
# helps['sql server firewall-rule allow-all-azure-ips'] = """
#             type: command
#             short-summary: Create a firewall rule that allows all Azure IP addresses to access the server.
#             """
helps['sql server firewall-rule create'] = """
            type: command
            short-summary: Creates a firewall rule.
            """
helps['sql server firewall-rule update'] = """
            type: command
            short-summary: Updates a firewall rule.
            """
helps['sql server firewall-rule show'] = """
            type: command
            short-summary: Shows the details of a firewall rule.
            """
helps['sql server firewall-rule list'] = """
            type: command
            short-summary: Lists the firewall rules.
            """
helps['sql server service-objective'] = """
            type: group
            short-summary: Show a server's service objectives.
            """
