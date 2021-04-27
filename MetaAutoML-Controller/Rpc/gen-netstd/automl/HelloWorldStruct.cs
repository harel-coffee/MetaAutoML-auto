/**
 * Autogenerated by Thrift Compiler (0.14.1)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using Thrift;
using Thrift.Collections;

using Thrift.Protocol;
using Thrift.Protocol.Entities;
using Thrift.Protocol.Utilities;
using Thrift.Transport;
using Thrift.Transport.Client;
using Thrift.Transport.Server;
using Thrift.Processor;


#pragma warning disable IDE0079  // remove unnecessary pragmas
#pragma warning disable IDE1006  // parts of the code use IDL spelling

namespace automl
{

  public partial class HelloWorldStruct : TBase
  {
    private string _text;

    public string Text
    {
      get
      {
        return _text;
      }
      set
      {
        __isset.text = true;
        this._text = value;
      }
    }


    public Isset __isset;
    public struct Isset
    {
      public bool text;
    }

    public HelloWorldStruct()
    {
    }

    public HelloWorldStruct DeepCopy()
    {
      var tmp0 = new HelloWorldStruct();
      if((Text != null) && __isset.text)
      {
        tmp0.Text = this.Text;
      }
      tmp0.__isset.text = this.__isset.text;
      return tmp0;
    }

    public async global::System.Threading.Tasks.Task ReadAsync(TProtocol iprot, CancellationToken cancellationToken)
    {
      iprot.IncrementRecursionDepth();
      try
      {
        TField field;
        await iprot.ReadStructBeginAsync(cancellationToken);
        while (true)
        {
          field = await iprot.ReadFieldBeginAsync(cancellationToken);
          if (field.Type == TType.Stop)
          {
            break;
          }

          switch (field.ID)
          {
            case 1:
              if (field.Type == TType.String)
              {
                Text = await iprot.ReadStringAsync(cancellationToken);
              }
              else
              {
                await TProtocolUtil.SkipAsync(iprot, field.Type, cancellationToken);
              }
              break;
            default: 
              await TProtocolUtil.SkipAsync(iprot, field.Type, cancellationToken);
              break;
          }

          await iprot.ReadFieldEndAsync(cancellationToken);
        }

        await iprot.ReadStructEndAsync(cancellationToken);
      }
      finally
      {
        iprot.DecrementRecursionDepth();
      }
    }

    public async global::System.Threading.Tasks.Task WriteAsync(TProtocol oprot, CancellationToken cancellationToken)
    {
      oprot.IncrementRecursionDepth();
      try
      {
        var struc = new TStruct("HelloWorldStruct");
        await oprot.WriteStructBeginAsync(struc, cancellationToken);
        var field = new TField();
        if((Text != null) && __isset.text)
        {
          field.Name = "text";
          field.Type = TType.String;
          field.ID = 1;
          await oprot.WriteFieldBeginAsync(field, cancellationToken);
          await oprot.WriteStringAsync(Text, cancellationToken);
          await oprot.WriteFieldEndAsync(cancellationToken);
        }
        await oprot.WriteFieldStopAsync(cancellationToken);
        await oprot.WriteStructEndAsync(cancellationToken);
      }
      finally
      {
        oprot.DecrementRecursionDepth();
      }
    }

    public override bool Equals(object that)
    {
      if (!(that is HelloWorldStruct other)) return false;
      if (ReferenceEquals(this, other)) return true;
      return ((__isset.text == other.__isset.text) && ((!__isset.text) || (System.Object.Equals(Text, other.Text))));
    }

    public override int GetHashCode() {
      int hashcode = 157;
      unchecked {
        if((Text != null) && __isset.text)
        {
          hashcode = (hashcode * 397) + Text.GetHashCode();
        }
      }
      return hashcode;
    }

    public override string ToString()
    {
      var sb = new StringBuilder("HelloWorldStruct(");
      int tmp1 = 0;
      if((Text != null) && __isset.text)
      {
        if(0 < tmp1++) { sb.Append(", "); }
        sb.Append("Text: ");
        Text.ToString(sb);
      }
      sb.Append(')');
      return sb.ToString();
    }
  }

}
