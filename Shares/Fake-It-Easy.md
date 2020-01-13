# Introduction of UnitTest framework FakeItEasy

## AAA Syntax

```c#
//Arrange

//Act

//Assert
```

## FakeItEasy Example

### Simple Verification

```csharp
  A.CallTo({lambda});

  A.CallTo(
    () => fakeRepo.Save(A<Customer>.Ignored))
    .MustHaveHappened(Reported.Exactly.Once);
  )
```

### Return Values

```csharp
  A.CallTo(
    () => fakeRepo.Save(A<Customer>.Ignored))
    .Returns(null);
  )
  A.CallTo(
    () => fakeRepo.Save(A<Customer>.Ignored))
    .Returns(new RuleTemplate());
  )
```

### Out Parameters

```csharp
//  _ruleFactory.TryParse(code, out ruleTemplate);
  // if(ruleTemplate == null) {
  //     throw new Exception();
  // }
  //do something with ruleTempalte
  A.CallTo(
    () => fakeRuleFactory.TryParse(A<string>.Ignored, out returnedRuleTemplate))
    .Returns(true)
    .AssignedOutAdnRefParameters(new RuleTemplate());
}
```

### Speicific parameters

Assert specific paramters are passed into function

``` c#
  //Assert
  A.CallTo(
    () => fakeRuleBuilder.Create(obj.code, obj.template))
    .MustHaveHappened();

  //or better
  A.CallTo(
    () => fakeRuleBuilder.Create(
      A<string>.That.Matches(s => s.Equals(obj.code)), 
      A<string>.That.Matches(s => s.Equals(obj.template))))
    .MustHaveHappened();
```

### Excptions

```c#
  A.CallTo(
    () => fakeRuleBuilder.Create(
      A<string>.That.Matches(s => s.Equals(obj.code)), 
      A<string>.That.Matches(s => s.Equals(obj.template))))
      .Throws(new Exception());
```

### Auto mocking Hierarchy

```c#
  // it will fake the call chain automatically
  A.CallTo(
    () => fakeApplicaitonSettings
          .SystemConfiguration
          .AuditingInformation
          .WorkstationId)
        .Returns(123);
```
