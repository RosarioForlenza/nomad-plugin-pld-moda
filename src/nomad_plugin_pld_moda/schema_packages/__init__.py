from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


# class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
#     parameter: int = Field(0, description='Custom configuration parameter')

#     def load(self):
#         from nomad_plugin_pld_moda.schema_packages.schema_package import m_package

#         return m_package


# schema_package_entry_point = NewSchemaPackageEntryPoint(
#     name='NewSchemaPackage',
#     description='New schema package entry point configuration.',
# )


class pld_schemaEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_plugin_pld_moda.schema_packages.pld_schema import m_package

        return m_package


pld_schema_entry_point = pld_schemaEntryPoint(
    name='PLD-MODA-LAB',
    description='Schema package for the description of the PLD-MODA instrument of the MODA laboratory of the CNR-SPIN of Naples.',
)

