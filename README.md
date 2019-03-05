DotNetCoreLambda
=====

AWS Lambda + .Net Core 2.1 Example

1. Create .NET Core Library (netcoreapp2.1)
2. Run: `dotnet add ./DotNetCoreLambda/DotNetCoreLambda.csproj package Amazon.Lambda.Core`
3. Run: `dotnet add ./DotNetCoreLambda/DotNetCoreLambda.csproj package Amazon.Lambda.Serialization.Json`
4. Modify .csproj file
  - Add `<GenerateRuntimeConfigurationFiles>true</GenerateRuntimeConfigurationFiles>` into `PropertyGroup` section 
4. Create ./DotNetCoreLambda/Function.cs
5. Run: `dotnet publish -c Release`
6. Run: `zip -j ~/Desktop/output.zip ./DotNetCoreLambda/bin/Release/netcoreapp2.1/publish/*`
7. Deploy out.zip

HandlerName: DotNetCoreLambda::DotNetCoreLambda.Function::FunctionHandler

## LICENSE

MIT

